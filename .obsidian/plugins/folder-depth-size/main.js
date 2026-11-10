const { ExtraButtonComponent, Menu, Plugin, PluginSettingTab, Setting } = require("obsidian");

// Classe du bouton « réglages des plugins » ajouté aux contrôles du graphe.
const CLASSE_BOUTON = "mod-pnd-reglages-plugins";

// Type donné par Folders to Graph à ses nœuds de dossiers, dont l'identifiant
// est le chemin précédé d'une barre : "/", "/Concepts", "/Concepts/Design".
const TYPE_DOSSIER = "f2g_node";

// Type donné par Obsidian aux nœuds de tag (option « Tags » du graphe), dont
// l'identifiant est le tag lui-même : "#year1".
const TYPE_TAG = "tag";

// Type donné par Obsidian aux nœuds de pièces jointes (option « Pièces
// jointes » du graphe), dont l'identifiant est le chemin du fichier :
// "Raw/Year 2/Probability/Cours 6 - T-Test.docx".
const TYPE_ATTACHEMENT = "attachment";

// Tailles exprimées dans l'unité du graphe d'Obsidian, où une note plafonne
// à 30 quel que soit son nombre de liens : un minimum au-dessus de 30 garde
// tout dossier plus gros que n'importe quelle note.
// Couleurs des dossiers : une par niveau à partir du niveau 1 ; la dernière
// vaut pour tous les niveaux plus profonds, et la racine « / » prend celle du
// niveau 1.
// Tags : sans réglage, Obsidian les dimensionne selon leur nombre de notes et
// leur donne à tous la couleur --graph-node-tag du thème.
// Pièces jointes : de même, taille selon leurs liens et couleur
// --graph-node-attachment ; la couleur se règle ici par extension.
const DEFAUTS = {
	tailleNiveau1: 60,
	ratio: 0.75,
	tailleMin: 32,
	colorer: false,
	couleurs: ["#ffd84d", "#ffb347", "#ff8c69", "#e07a9f"],
	tagsTaille: false,
	tailleTag: 40,
	tagsCouleur: false,
	couleurTagDefaut: "#ff9f1c",
	couleursTags: {},
	attachementsTaille: false,
	tailleAttachement: 20,
	attachementsCouleur: false,
	couleurAttachementDefaut: "#a0a0a0",
	couleursExtensions: {},
	modeNoms: "fixe",
	tailleNoms: 100,
	seuilNoms: 0,
	// Niveaux dont le nom s'affiche, par profondeur ("1", "2"…) : un niveau
	// absent vaut true, pour que les dossiers plus profonds créés plus tard
	// s'affichent sans réglage.
	niveauxNoms: {},
	cheminNoms: "relatif",
};

// Texte affiché sous un dossier : son nom seul, ou son chemin depuis la racine.
const CHEMINS_NOMS = {
	relatif: "Nom du dossier (Peinture)",
	complet: "Chemin complet (Cours/Design/Peinture)",
};

// Identifiant Folders to Graph ("/Cours/Design") vers le texte voulu.
function texteDossier(id, mode) {
	const parties = String(id).split("/").filter(Boolean);
	if (parties.length === 0) return "/";
	return mode === "complet" ? parties.join("/") : parties[parties.length - 1];
}

// Modes d'affichage du nom des dossiers.
const MODES_NOMS = {
	obsidian: "Comme les notes : disparaît en dézoomant, selon un seuil",
	visible: "Toujours visible, rapetisse avec le zoom",
	fixe: "Toujours visible, taille fixe à l'écran",
};

function profondeur(noeud) {
	return String(noeud.id).split("/").filter(Boolean).length;
}

function enRgb(hex) {
	const rgb = parseInt(String(hex).replace("#", ""), 16);
	return Number.isNaN(rgb) ? undefined : { a: 1, rgb };
}

// Les tags ne tiennent pas compte de la casse dans Obsidian : on range leurs
// couleurs sous une clé en minuscules.
function cleTag(tag) {
	return String(tag).toLowerCase();
}

// Extension d'un chemin, en minuscules et sans le point : "docx". Vide si le
// nom n'en a pas (ou ne commence que par un point, comme ".gitignore").
function extension(chemin) {
	const nom = String(chemin).split("/").pop();
	const point = nom.lastIndexOf(".");
	return point > 0 ? nom.slice(point + 1).toLowerCase() : "";
}

module.exports = class PersonnalisationNoeudsDossiers extends Plugin {
	async onload() {
		const donnees = (await this.loadData()) || {};
		this.reglages = Object.assign({}, DEFAUTS, donnees);
		if (!Array.isArray(this.reglages.couleurs) || this.reglages.couleurs.length === 0) {
			this.reglages.couleurs = DEFAUTS.couleurs.slice();
		}
		// Anciennes cases à cocher (versions précédentes) : on les traduit en mode.
		if (!("modeNoms" in donnees) && "nomsDossiers" in donnees) {
			this.reglages.modeNoms = !donnees.nomsDossiers ? "obsidian" : donnees.nomsLisibles === false ? "visible" : "fixe";
		}
		delete this.reglages.nomsDossiers;
		delete this.reglages.nomsLisibles;
		if (!(this.reglages.modeNoms in MODES_NOMS)) this.reglages.modeNoms = DEFAUTS.modeNoms;
		if (!Number.isFinite(this.reglages.seuilNoms)) this.reglages.seuilNoms = DEFAUTS.seuilNoms;
		if (!(this.reglages.cheminNoms in CHEMINS_NOMS)) this.reglages.cheminNoms = DEFAUTS.cheminNoms;
		for (const cle of ["couleursTags", "couleursExtensions", "niveauxNoms"]) {
			if (!this.reglages[cle] || typeof this.reglages[cle] !== "object") this.reglages[cle] = {};
		}
		this.actif = true;
		// Nos enveloppes, pour savoir si la méthode d'un prototype est encore la nôtre.
		this.enveloppes = new WeakSet();
		this.restaurations = [];

		this.addSettingTab(new OngletReglages(this.app, this));
		this.app.workspace.onLayoutReady(() => this.appliquer());
		this.registerEvent(this.app.workspace.on("layout-change", () => this.appliquer()));
		// Le graphe crée ses nœuds après l'ouverture de la vue : on repasse
		// régulièrement jusqu'à trouver des nœuds à patcher. Le coût est nul
		// une fois le prototype patché.
		this.registerInterval(window.setInterval(() => this.appliquer(), 2000));
	}

	onunload() {
		this.actif = false;
		for (const restaurer of this.restaurations) restaurer();
		// Rend aux dossiers le texte d'origine, que nous avons pu remplacer.
		for (const vue of this.vuesGraphe()) {
			for (const noeud of vue.renderer.nodes ?? []) {
				if (noeud.type === TYPE_DOSSIER && noeud.text && typeof noeud.getDisplayText === "function") {
					noeud.text.text = noeud.getDisplayText();
				}
			}
		}
		document.querySelectorAll(`.${CLASSE_BOUTON}`).forEach((el) => el.remove());
		this.rafraichir();
	}

	// Ajoute le bouton en dernier dans les contrôles du graphe, donc sous les
	// icônes des autres plugins. Ceux-ci peuvent ajouter les leurs plus tard
	// (Extended Graph, à son activation) : à chaque passage, le bouton est
	// redescendu en dernière position s'il ne l'est plus.
	placerBouton(vue) {
		const controles = vue.contentEl?.querySelector(".graph-controls");
		if (!controles) return;
		const existant = controles.querySelector(`.${CLASSE_BOUTON}`);
		if (existant) {
			if (controles.lastElementChild !== existant) controles.appendChild(existant);
			return;
		}
		new ExtraButtonComponent(controles)
			.setIcon("sliders-horizontal")
			.setTooltip("Réglages des plugins")
			.then((b) => {
				b.extraSettingsEl.addClasses(["graph-controls-button", CLASSE_BOUTON]);
				b.extraSettingsEl.addEventListener("click", (evt) => this.menuReglages(evt));
			});
	}

	// Liste les plugins communautaires activés qui ont un onglet de réglages,
	// relue à chaque ouverture pour suivre les installations et activations.
	menuReglages(evt) {
		const reglages = this.app.setting;
		const actives = this.app.plugins?.enabledPlugins;
		const onglets = (reglages?.pluginTabs ?? [])
			.filter((onglet) => !actives || actives.has(onglet.id))
			.sort((a, b) => a.name.localeCompare(b.name, "fr"));

		const menu = new Menu();
		if (onglets.length === 0) {
			menu.addItem((item) => item.setTitle("Aucun plugin avec des réglages").setDisabled(true));
		}
		for (const onglet of onglets) {
			menu.addItem((item) =>
				item.setTitle(onglet.name).setIcon("settings").onClick(() => {
					reglages.open();
					reglages.openTabById(onglet.id);
				})
			);
		}
		menu.showAtMouseEvent(evt);
	}

	vuesGraphe() {
		return ["graph", "localgraph"]
			.flatMap((type) => this.app.workspace.getLeavesOfType(type))
			.map((feuille) => feuille.view)
			.filter((vue) => vue && vue.renderer);
	}

	// Folders to Graph patche le même prototype, une seule fois, quand le
	// graphe reçoit ses données : s'il passe après nous, son getFillColor
	// répond pour les dossiers sans appeler le nôtre. On se remet donc
	// au-dessus à chaque passage dès que la méthode n'est plus la nôtre.
	appliquer() {
		for (const vue of this.vuesGraphe()) {
			this.placerBouton(vue);
			const noeuds = vue.renderer.nodes;
			if (!noeuds || noeuds.length === 0) continue;
			const proto = Object.getPrototypeOf(noeuds[0]);
			const tailleOk = this.auDessus(proto, "getSize", (n) => this.taille(n));
			const couleurOk = this.auDessus(proto, "getFillColor", (n) => this.couleur(n));
			const renduOk = this.envelopperRendu(proto);
			if (tailleOk || couleurOk || renduOk) vue.renderer.changed?.();
		}
	}

	// Enveloppe proto[methode] si elle n'est pas déjà notre enveloppe.
	// Renvoie true si une enveloppe a été posée.
	auDessus(proto, methode, calcul) {
		if (this.enveloppes.has(proto[methode])) return false;
		return this.envelopper(proto, methode, calcul);
	}

	// Remplace proto[methode]. `calcul` renvoie la valeur à utiliser pour ce
	// nœud, ou undefined pour laisser la méthode d'origine (Folders to Graph
	// ou Obsidian) répondre : c'est le cas de tout nœud qui n'est ni un dossier
	// ni un tag, et des réglages désactivés.
	envelopper(proto, methode, calcul) {
		const original = proto[methode];
		if (typeof original !== "function") return false;
		const plugin = this;
		const remplacant = function (...args) {
			if (plugin.actif) {
				const valeur = calcul(this);
				if (valeur !== undefined) return valeur;
			}
			return original.apply(this, args);
		};
		proto[methode] = remplacant;
		this.enveloppes.add(remplacant);
		// Si un autre plugin a enveloppé la méthode après nous, on ne peut pas
		// défaire la chaîne : `actif` à false suffit alors à rendre la main.
		this.restaurations.push(() => {
			if (proto[methode] === remplacant) proto[methode] = original;
		});
		return true;
	}

	// Obsidian recalcule l'étiquette de chaque nœud à chaque image, dans
	// render() : opacité selon le zoom et le « seuil d'apparition du texte »,
	// estompage quand un autre nœud est survolé, taille réduite quand on
	// dézoome. On laisse faire, puis on rétablit le nom des dossiers.
	envelopperRendu(proto) {
		const original = proto.render;
		if (typeof original !== "function" || this.enveloppes.has(original)) return false;
		const plugin = this;
		const remplacant = function (...args) {
			const resultat = original.apply(this, args);
			if (plugin.actif && this.type === TYPE_DOSSIER) {
				plugin.afficherNom(this);
			}
			return resultat;
		};
		proto.render = remplacant;
		this.enveloppes.add(remplacant);
		this.restaurations.push(() => {
			if (proto.render === remplacant) proto.render = original;
		});
		return true;
	}

	// Modes « toujours visible » : reprend le placement d'Obsidian (sous le
	// cercle, décalé si le nœud est survolé), en forçant la visibilité et
	// l'opacité. En mode « fixe », le texte garde la même taille à l'écran
	// quel que soit le zoom, comme le nom du nœud survolé chez Obsidian ; en
	// mode « visible », il suit l'échelle des notes. La taille réglée
	// multiplie l'une ou l'autre.
	afficherNom(noeud) {
		const { renderer: graphe, text: texte, circle: cercle } = noeud;
		if (!noeud.rendered || !texte || !graphe) return;
		const r = this.reglages;
		const facteur = r.tailleNoms / 100;
		// Obsidian n'écrit le texte qu'à la création du nœud : on le remplace
		// ici, seulement quand il change (un nouveau texte coûte un rendu PIXI).
		const voulu = texteDossier(noeud.id, r.cheminNoms);
		if (texte.text !== voulu) texte.text = voulu;
		// Niveau masqué : pas de nom, sauf pour le dossier survolé, qu'Obsidian
		// a déjà affiché.
		if (!this.niveauAffiche(noeud)) {
			if (graphe.getHighlightNode?.() !== noeud) texte.visible = false;
			return;
		}
		// Mode « comme les notes » : même calcul qu'Obsidian, avec notre seuil.
		if (r.modeNoms === "obsidian") {
			this.nomSelonSeuil(noeud, facteur);
			return;
		}
		// Cercle hors de la zone visible : Obsidian l'a masqué, le nom suit.
		if (cercle && !cercle.visible) {
			texte.visible = false;
			return;
		}
		const echelleNoeud = graphe.nodeScale ?? 1;
		const zoom = graphe.scale || 1;
		const base = r.modeNoms === "fixe" && zoom < 1 ? 1 / zoom : echelleNoeud;
		const echelle = base * facteur;
		texte.visible = true;
		texte.x = noeud.x;
		texte.y = noeud.y + (noeud.getSize() + 5) * echelleNoeud + (noeud.moveText || 0) / zoom;
		texte.scale.x = texte.scale.y = echelle;
		texte.alpha = graphe.colors?.text?.a ?? 1;
	}

	// La racine « / » (profondeur 0) suit le niveau 1, comme pour les couleurs.
	niveauAffiche(noeud) {
		const niveau = Math.max(profondeur(noeud), 1);
		return this.reglages.niveauxNoms[String(niveau)] !== false;
	}

	// Dossiers du coffre par profondeur, pour les réglages : { 1: [...], 2: [...] }.
	// Les dossiers que Folders to Graph exclut du graphe (Raw ici) sont écartés,
	// ainsi que les dossiers cachés.
	dossiersParNiveau() {
		const f2g = this.app.plugins?.plugins?.folders2graph?.settings;
		const exclus = f2g?.folderFilterMode === "exclude" ? (f2g.folderFilterList ?? []) : [];
		const inclus = f2g?.folderFilterMode === "include" ? (f2g.folderFilterList ?? []) : null;
		const sous = (chemin, racine) => chemin === racine || chemin.startsWith(racine + "/");
		const niveaux = {};
		for (const fichier of this.app.vault.getAllLoadedFiles?.() ?? []) {
			if (!fichier.children || !fichier.path || fichier.path === "/") continue;
			const chemin = fichier.path;
			if (chemin.split("/").some((p) => p.startsWith("."))) continue;
			if (exclus.some((e) => sous(chemin, e))) continue;
			if (inclus && !inclus.some((e) => sous(chemin, e))) continue;
			const niveau = chemin.split("/").length;
			(niveaux[niveau] ??= []).push(chemin);
		}
		for (const liste of Object.values(niveaux)) liste.sort((a, b) => a.localeCompare(b, "fr"));
		return niveaux;
	}

	// Reprend la règle d'Obsidian pour les noms (setScale puis render) :
	// opacité = log2(zoom) + 1 − seuil, bornée entre 0 et 1, multipliée par
	// l'estompage du survol ; le nœud survolé garde toujours son nom. Seul le
	// seuil diffère : celui du plugin au lieu du « seuil d'apparition du
	// texte » du graphe, qui continue de régler les notes.
	nomSelonSeuil(noeud, facteur) {
		const { renderer: graphe, text: texte, circle: cercle } = noeud;
		const zoom = graphe.scale || 1;
		const survole = graphe.getHighlightNode?.() === noeud;
		let alpha = Math.min(1, Math.max(0, Math.log2(zoom) + 1 - this.reglages.seuilNoms));
		alpha *= noeud.fadeAlpha ?? 1;
		if (survole) alpha = 1;
		alpha *= graphe.colors?.text?.a ?? 1;
		const visible = alpha > 0.001 && (!cercle || cercle.visible);
		texte.visible = visible;
		if (!visible) return;
		const echelleNoeud = graphe.nodeScale ?? 1;
		const echelle = survole && zoom < 1 ? 1 / zoom : echelleNoeud;
		texte.x = noeud.x;
		texte.y = noeud.y + (noeud.getSize() + 5) * echelleNoeud + (noeud.moveText || 0) / zoom;
		texte.scale.x = texte.scale.y = echelle * facteur;
		texte.alpha = alpha;
	}

	taille(noeud) {
		const r = this.reglages;
		const mult = noeud.renderer?.fNodeSizeMult ?? 1;
		if (noeud.type === TYPE_DOSSIER) {
			return Math.max(r.tailleMin, r.tailleNiveau1 * Math.pow(r.ratio, profondeur(noeud) - 1)) * mult;
		}
		if (noeud.type === TYPE_TAG && r.tagsTaille) return r.tailleTag * mult;
		if (noeud.type === TYPE_ATTACHEMENT && r.attachementsTaille) return r.tailleAttachement * mult;
		return undefined;
	}

	couleur(noeud) {
		const r = this.reglages;
		if (noeud.type === TYPE_DOSSIER && r.colorer) {
			const indice = Math.min(Math.max(profondeur(noeud), 1), r.couleurs.length) - 1;
			return enRgb(r.couleurs[indice]);
		}
		if (noeud.type === TYPE_TAG && r.tagsCouleur) {
			return enRgb(r.couleursTags[cleTag(noeud.id)] ?? r.couleurTagDefaut);
		}
		if (noeud.type === TYPE_ATTACHEMENT && r.attachementsCouleur) {
			return enRgb(r.couleursExtensions[extension(noeud.id)] ?? r.couleurAttachementDefaut);
		}
		return undefined;
	}

	// Extensions des fichiers du coffre autres que les notes, triées, pour
	// proposer une couleur par type de pièce jointe.
	extensionsDuCoffre() {
		const vues = new Set();
		for (const fichier of this.app.vault.getFiles()) {
			const ext = extension(fichier.path);
			if (ext && ext !== "md") vues.add(ext);
		}
		return [...vues].sort((a, b) => a.localeCompare(b, "fr"));
	}

	// Tags du coffre, triés, pour proposer une couleur par tag.
	tagsDuCoffre() {
		const tags = this.app.metadataCache.getTags?.() ?? {};
		const vus = new Map();
		for (const tag of Object.keys(tags)) {
			if (!vus.has(cleTag(tag))) vus.set(cleTag(tag), tag);
		}
		return [...vus.values()].sort((a, b) => a.localeCompare(b, "fr", { numeric: true }));
	}

	rafraichir() {
		for (const vue of this.vuesGraphe()) vue.renderer.changed?.();
	}

	async enregistrer() {
		await this.saveData(this.reglages);
		this.rafraichir();
	}
};

class OngletReglages extends PluginSettingTab {
	constructor(app, plugin) {
		super(app, plugin);
		this.plugin = plugin;
	}

	display() {
		const { containerEl } = this;
		containerEl.empty();
		this.sectionTaille(containerEl);
		this.sectionCouleur(containerEl);
		this.sectionNoms(containerEl);
		this.sectionTags(containerEl);
		this.sectionAttachements(containerEl);
	}

	sectionTaille(containerEl) {
		const r = this.plugin.reglages;
		new Setting(containerEl).setName("Taille des dossiers").setHeading();

		containerEl.createEl("p", {
			text: "Une note du graphe mesure au plus 30. Le dossier racine « / », s'il est affiché, prend la taille du niveau 1 divisée par le ratio.",
		});

		new Setting(containerEl)
			.setName("Taille du niveau 1")
			.setDesc("Taille des dossiers à la racine du coffre, comme Concepts ou Cours.")
			.addSlider((s) =>
				s.setLimits(32, 150, 2).setValue(r.tailleNiveau1).setDynamicTooltip()
					.onChange(async (v) => { r.tailleNiveau1 = v; await this.plugin.enregistrer(); })
			);

		new Setting(containerEl)
			.setName("Ratio par niveau")
			.setDesc("Chaque niveau plus profond multiplie la taille par ce ratio.")
			.addSlider((s) =>
				s.setLimits(0.4, 1, 0.05).setValue(r.ratio).setDynamicTooltip()
					.onChange(async (v) => { r.ratio = v; await this.plugin.enregistrer(); })
			);

		new Setting(containerEl)
			.setName("Taille minimale d'un dossier")
			.setDesc("Plancher pour les dossiers profonds. Au-dessus de 30, un dossier reste plus gros que toute note.")
			.addSlider((s) =>
				s.setLimits(8, 60, 1).setValue(r.tailleMin).setDynamicTooltip()
					.onChange(async (v) => { r.tailleMin = v; await this.plugin.enregistrer(); })
			);
	}

	sectionCouleur(containerEl) {
		const r = this.plugin.reglages;
		new Setting(containerEl).setName("Couleur des dossiers").setHeading();

		new Setting(containerEl)
			.setName("Colorer les dossiers par profondeur")
			.setDesc("Désactivé, les dossiers gardent la couleur réglée dans Folders to Graph.")
			.addToggle((t) =>
				t.setValue(r.colorer).onChange(async (v) => {
					r.colorer = v;
					await this.plugin.enregistrer();
					this.display();
				})
			);

		if (!r.colorer) return;

		r.couleurs.forEach((couleur, i) => {
			const dernier = i === r.couleurs.length - 1;
			const nom = dernier && i > 0 ? `Niveau ${i + 1} et plus` : `Niveau ${i + 1}`;
			const reglage = new Setting(containerEl)
				.setName(nom)
				.setDesc(i === 0 ? "Vaut aussi pour la racine « / »." : "")
				.addColorPicker((c) =>
					c.setValue(couleur).onChange(async (v) => {
						r.couleurs[i] = v;
						await this.plugin.enregistrer();
					})
				);
			if (r.couleurs.length > 1) {
				reglage.addExtraButton((b) =>
					b.setIcon("trash").setTooltip("Retirer ce niveau").onClick(async () => {
						r.couleurs.splice(i, 1);
						await this.plugin.enregistrer();
						this.display();
					})
				);
			}
		});

		new Setting(containerEl).addButton((b) =>
			b.setButtonText("Ajouter un niveau").onClick(async () => {
				r.couleurs.push(r.couleurs[r.couleurs.length - 1]);
				await this.plugin.enregistrer();
				this.display();
			})
		);
	}

	sectionNoms(containerEl) {
		const r = this.plugin.reglages;
		new Setting(containerEl).setName("Noms des dossiers").setHeading();

		new Setting(containerEl)
			.setName("Affichage")
			.setDesc("Les notes gardent toujours le comportement d'Obsidian. « Toujours visible » ignore le zoom, le seuil d'apparition du texte et le survol d'un autre nœud.")
			.addDropdown((d) => {
				for (const [cle, libelle] of Object.entries(MODES_NOMS)) d.addOption(cle, libelle);
				d.setValue(r.modeNoms).onChange(async (v) => {
					r.modeNoms = v;
					await this.plugin.enregistrer();
					this.display();
				});
			});

		if (r.modeNoms === "obsidian") {
			new Setting(containerEl)
				.setName("Seuil de zoom")
				.setDesc("Plus la valeur est basse, plus les noms restent visibles en dézoomant. Même échelle que le « seuil d'apparition du texte » du graphe (0 par défaut), qui continue de régler les notes ; un graphe très dézoomé demande une valeur négative.")
				.addSlider((s) =>
					s.setLimits(-8, 3, 0.1).setValue(r.seuilNoms).setDynamicTooltip()
						.onChange(async (v) => { r.seuilNoms = v; await this.plugin.enregistrer(); })
				);
		}

		new Setting(containerEl)
			.setName("Chemin affiché")
			.setDesc("Le nom seul du dossier, ou son chemin depuis la racine du coffre.")
			.addDropdown((d) => {
				for (const [cle, libelle] of Object.entries(CHEMINS_NOMS)) d.addOption(cle, libelle);
				d.setValue(r.cheminNoms).onChange(async (v) => {
					r.cheminNoms = v;
					await this.plugin.enregistrer();
				});
			});

		this.reglagesNiveaux(containerEl);

		new Setting(containerEl)
			.setName("Taille des noms")
			.setDesc("En pourcentage de la taille normale d'un nom, dans les trois modes.")
			.addSlider((s) =>
				s.setLimits(40, 400, 10).setValue(r.tailleNoms).setDynamicTooltip()
					.onChange(async (v) => { r.tailleNoms = v; await this.plugin.enregistrer(); })
			);
	}

	// Une case par niveau de dossier présent dans le graphe, avec des exemples.
	// Un niveau décoché n'affiche plus de nom, sauf au survol.
	reglagesNiveaux(containerEl) {
		const r = this.plugin.reglages;
		const niveaux = this.plugin.dossiersParNiveau();
		const profondeurs = Object.keys(niveaux).map(Number).sort((a, b) => a - b);
		if (profondeurs.length === 0) return;

		containerEl.createEl("p", {
			text: "Niveaux dont le nom s'affiche. Un niveau décoché ne montre son nom qu'au survol.",
		});

		for (const niveau of profondeurs) {
			const dossiers = niveaux[niveau];
			const noms = dossiers.slice(0, 4).join(", ") + (dossiers.length > 4 ? "…" : "");
			new Setting(containerEl)
				.setName(`Niveau ${niveau} (${dossiers.length} dossier${dossiers.length > 1 ? "s" : ""})`)
				.setDesc(noms)
				.addToggle((t) =>
					t.setValue(r.niveauxNoms[String(niveau)] !== false).onChange(async (v) => {
						r.niveauxNoms[String(niveau)] = v;
						await this.plugin.enregistrer();
					})
				);
		}
	}

	sectionTags(containerEl) {
		const r = this.plugin.reglages;
		new Setting(containerEl).setName("Tags").setHeading();

		containerEl.createEl("p", {
			text: "S'applique aux nœuds de tag, visibles quand l'option « Tags » du graphe est activée.",
		});

		new Setting(containerEl)
			.setName("Taille fixe pour les tags")
			.setDesc("Désactivé, Obsidian dimensionne chaque tag selon son nombre de notes (30 au plus).")
			.addToggle((t) =>
				t.setValue(r.tagsTaille).onChange(async (v) => {
					r.tagsTaille = v;
					await this.plugin.enregistrer();
					this.display();
				})
			);

		if (r.tagsTaille) {
			new Setting(containerEl)
				.setName("Taille des tags")
				.addSlider((s) =>
					s.setLimits(4, 120, 1).setValue(r.tailleTag).setDynamicTooltip()
						.onChange(async (v) => { r.tailleTag = v; await this.plugin.enregistrer(); })
				);
		}

		new Setting(containerEl)
			.setName("Colorer les tags")
			.setDesc("Désactivé, tous les tags gardent la couleur du thème.")
			.addToggle((t) =>
				t.setValue(r.tagsCouleur).onChange(async (v) => {
					r.tagsCouleur = v;
					await this.plugin.enregistrer();
					this.display();
				})
			);

		if (!r.tagsCouleur) return;

		new Setting(containerEl)
			.setName("Couleur par défaut")
			.setDesc("Pour les tags sans couleur propre, y compris ceux créés plus tard.")
			.addColorPicker((c) =>
				c.setValue(r.couleurTagDefaut).onChange(async (v) => {
					r.couleurTagDefaut = v;
					await this.plugin.enregistrer();
				})
			);

		const tags = this.plugin.tagsDuCoffre();
		if (tags.length === 0) {
			containerEl.createEl("p", { text: "Aucun tag dans le coffre." });
			return;
		}
		for (const tag of tags) {
			const cle = cleTag(tag);
			const propre = r.couleursTags[cle];
			const reglage = new Setting(containerEl)
				.setName(tag)
				.setDesc(propre ? "" : "Couleur par défaut")
				.addColorPicker((c) =>
					c.setValue(propre ?? r.couleurTagDefaut).onChange(async (v) => {
						r.couleursTags[cle] = v;
						await this.plugin.enregistrer();
						reglage.setDesc("");
					})
				);
			if (propre) {
				reglage.addExtraButton((b) =>
					b.setIcon("rotate-ccw").setTooltip("Revenir à la couleur par défaut").onClick(async () => {
						delete r.couleursTags[cle];
						await this.plugin.enregistrer();
						this.display();
					})
				);
			}
		}
	}

	sectionAttachements(containerEl) {
		const r = this.plugin.reglages;
		new Setting(containerEl).setName("Pièces jointes").setHeading();

		containerEl.createEl("p", {
			text: "S'applique aux nœuds de pièces jointes (PDF, Word, images…), visibles quand l'option « Pièces jointes » du graphe est activée.",
		});

		new Setting(containerEl)
			.setName("Taille fixe pour les pièces jointes")
			.setDesc("Désactivé, Obsidian dimensionne chaque pièce jointe selon ses liens (30 au plus).")
			.addToggle((t) =>
				t.setValue(r.attachementsTaille).onChange(async (v) => {
					r.attachementsTaille = v;
					await this.plugin.enregistrer();
					this.display();
				})
			);

		if (r.attachementsTaille) {
			new Setting(containerEl)
				.setName("Taille des pièces jointes")
				.addSlider((s) =>
					s.setLimits(4, 120, 1).setValue(r.tailleAttachement).setDynamicTooltip()
						.onChange(async (v) => { r.tailleAttachement = v; await this.plugin.enregistrer(); })
				);
		}

		new Setting(containerEl)
			.setName("Colorer les pièces jointes")
			.setDesc("Désactivé, toutes les pièces jointes gardent la couleur du thème.")
			.addToggle((t) =>
				t.setValue(r.attachementsCouleur).onChange(async (v) => {
					r.attachementsCouleur = v;
					await this.plugin.enregistrer();
					this.display();
				})
			);

		if (!r.attachementsCouleur) return;

		new Setting(containerEl)
			.setName("Couleur par défaut")
			.setDesc("Pour les extensions sans couleur propre, y compris celles ajoutées plus tard.")
			.addColorPicker((c) =>
				c.setValue(r.couleurAttachementDefaut).onChange(async (v) => {
					r.couleurAttachementDefaut = v;
					await this.plugin.enregistrer();
				})
			);

		const extensions = this.plugin.extensionsDuCoffre();
		if (extensions.length === 0) {
			containerEl.createEl("p", { text: "Aucune pièce jointe dans le coffre." });
			return;
		}
		for (const ext of extensions) {
			const propre = r.couleursExtensions[ext];
			const reglage = new Setting(containerEl)
				.setName(`.${ext}`)
				.setDesc(propre ? "" : "Couleur par défaut")
				.addColorPicker((c) =>
					c.setValue(propre ?? r.couleurAttachementDefaut).onChange(async (v) => {
						r.couleursExtensions[ext] = v;
						await this.plugin.enregistrer();
						reglage.setDesc("");
					})
				);
			if (propre) {
				reglage.addExtraButton((b) =>
					b.setIcon("rotate-ccw").setTooltip("Revenir à la couleur par défaut").onClick(async () => {
						delete r.couleursExtensions[ext];
						await this.plugin.enregistrer();
						this.display();
					})
				);
			}
		}
	}
}
