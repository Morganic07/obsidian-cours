---
type: source
tags: [year4]
sources: ["[[Raw/Year 4/histoire du design et interactions /chp2 cours.pdf|chp2 cours.pdf]]"]
maj: 2026-11-10
complet: true
enrichi: 2026-11-10
---

Résumé de [[Raw/Year 4/histoire du design et interactions /chp2 cours.pdf|chp2 cours.pdf]], dans [[Cours/Design/Histoire du design/_index|Histoire du design]]. Support de 40 pages en paysage, qui suit le [[1 - Histoire du design|chapitre 1]] ([[Cybernétique|cybernétique]], [[Contre-culture|contre-culture]]). Il se compose de cinq ensembles :

1. pages 1 à 8 : repères sur [[ARPANET]], le [[Courrier électronique|courrier électronique]], [[Xerox PARC]], la [[Silicon Valley]] et le [[World Wide Web|Web]] ;
2. pages 9 à 17 : une fiche de lecture d'un chapitre intitulé « Du réseau informatique au World Wide Web » (l'auteur et l'ouvrage ne sont pas nommés) ;
3. pages 18 et 19 : une grande chronologie, les personnages et les concepts à retenir, repris du chapitre 1 ;
4. pages 20 à 25 : six diapositives illustrées ([[Modem|modem]], messageries, portails, Menlo Park, cybernétique, *[[Whole Earth Catalog]]*) ;
5. pages 26 à 38 : une fiche de lecture du chapitre « La tragédie de la communication », qui résume le texte scanné de [[2 - De courrier à courriels]] (synthèse de l'utilisatrice : [[2 - Prise de note de courrier à courriel]]).

Les pages 39 et 40 sont vides. Le support renvoie à deux vidéos YouTube (sur Xerox PARC, page 5 ; un documentaire sur la Silicon Valley, page 7).

## 1. ARPANET : connecter des ordinateurs

À la fin des années 1960, [[ARPANET]] relie des centres de recherche américains. Le **29 octobre 1969**, un premier message est transmis de l'université de Californie à Los Angeles (**UCLA**) au **Stanford Research Institute ([[SRI International|SRI]])** : il est possible de faire communiquer des ordinateurs éloignés.

La question technique devient alors : comment faire communiquer **plusieurs [[Réseau|réseaux]] différents** entre eux ? Les [[Protocole de communication|protocoles]] **TCP/IP** ([[Suite des protocoles Internet]]) y répondent ; leur adoption par ARPANET en **1983** est un jalon dans la formation d'[[Internet]] comme « réseau de réseaux ».

*Figure : la carte d'ARPANET à ses débuts (1969), quatre [[Nœud (réseau)|nœuds]] sur la côte ouest et des liaisons vers la côte est.*
![[2 - Histoire du design - p2a.jpg]]

**Fiche ARPANET (page 2).** ARPANET est le premier réseau informatique à [[Commutation de paquets|commutation de paquets]], reconnu comme l'ancêtre direct d'Internet. Il est conçu par l'**ARPA** (*Advanced Research Projects Agency*, l'agence de recherche du [[Département de la Défense des États-Unis|département de la Défense des États-Unis]], renommée [[DARPA]] en 1972) et mis en service le 29 octobre 1969. [[Erreurs du cours#^e-2-histoire-du-design|✎]]

- **Création et premier message** : le premier message, « lo » (pour « login »), est envoyé le 29 octobre 1969 entre l'UCLA et l'Institut de recherche de Stanford.
- **Innovation majeure** : la commutation de paquets découpe les données en morceaux envoyés par des chemins multiples, ce qui garantit qu'un réseau reste fonctionnel même si une partie est détruite.
- **Évolution** : l'adoption des protocoles TCP/IP au début des années 1980 unifie la communication et prépare l'ère d'Internet.
- **Fermeture** : ARPANET cesse définitivement ses activités en 1990.

Le message « lo » est un accident : l'étudiant de l'équipe de Leonard Kleinrock à l'UCLA voulait taper « login », et le système du SRI s'est arrêté après deux lettres ; la connexion complète a réussi environ une heure plus tard. Le premier nœud (un [[Routeur|routeur]] appelé IMP, *[[Interface Message Processor]]*, construit par la société [[BBN]]) avait été installé à l'UCLA fin août 1969 ; en décembre 1969, le réseau compte quatre nœuds : UCLA, SRI, l'université de Californie à Santa Barbara et l'université de l'Utah. [[Complément hors du cours|ⓘ]]

L'argument de la survie à une attaque nucléaire est à nuancer : il motivait les travaux de Paul Baran ([[RAND Corporation|RAND]], 1960-1964) sur le [[Réseau décentralisé|réseau distribué]], l'une des deux origines de la commutation de paquets avec ceux de Donald Davies (laboratoire national de physique britannique, 1965), mais ARPANET a été financé pour partager des ressources de calcul entre centres de recherche. [[Complément hors du cours|ⓘ]]

L'ARPA elle-même est née de la [[Guerre froide]] : le gouvernement Eisenhower la crée en février 1958, quatre mois après le lancement du satellite soviétique [[Spoutnik]] (octobre 1957), pour que les États-Unis ne soient plus distancés technologiquement. Son bureau chargé de l'informatique, dirigé à partir de 1962 par J. C. R. Licklider, finance les recherches sur l'informatique interactive, le [[Temps partagé|temps partagé]] et les réseaux, qui mènent à ARPANET ([[Symbiose homme-machine]]). [[Complément hors du cours|ⓘ]]

*Figure : carte logique d'ARPANET en mars 1977 ; chaque boîte est un ordinateur relié à un IMP, le réseau s'étend d'un océan à l'autre et jusqu'à Hawaï par [[Satellite de télécommunications|satellite]].*
![[2 - Histoire du design - p2b.jpg]]

## Le courrier électronique de Ray Tomlinson

En **1971**, chez **[[BBN]]** (Bolt Beranek and Newman, l'entreprise qui construit les [[Interface Message Processor|IMP]] d'[[ARPANET]]), Ray Tomlinson adapte des programmes existants pour envoyer un message d'un ordinateur à un autre sur ARPANET. Il choisit le signe **@** ([[Arobase]]) pour séparer le nom de la personne de celui de la machine destinataire : `utilisateur@ordinateur`. Des messages électroniques existaient déjà entre utilisateurs d'un même ordinateur ; son apport concerne leur envoi **à travers le réseau** ([[Courrier électronique]]).

Tomlinson a combiné SNDMSG, qui déposait un message dans la boîte d'un autre utilisateur de la même machine (sous le [[Système d'exploitation|système d'exploitation]] à [[Temps partagé|temps partagé]] [[TENEX]]), et CPYNET, un programme de copie de fichiers par le réseau. Il a choisi @ parce que ce signe, présent sur les [[Disposition du clavier|claviers]], n'apparaissait dans aucun nom de personne ni de machine, et qu'il se lit « at » (« chez »). [[Complément hors du cours|ⓘ]]

Frise du support :

| Date | Repère | Ce que cela change |
|---|---|---|
| 1969 | Premiers échanges sur [[ARPANET]] | Des ordinateurs éloignés peuvent communiquer. |
| 1971 | [[Courrier électronique\|Courrier électronique]] de Ray Tomlinson | Des personnes peuvent s'adresser des messages par le réseau. |
| 1973 | Xerox Alto et travaux sur [[Ethernet]] à [[Xerox PARC\|PARC]] | L'[[Ordinateur personnel\|ordinateur personnel]] connecté devient un objet de recherche concret. |
| 1989 | Proposition du Web au [[CERN]] | Les documents pourront être reliés et parcourus par [[Lien hypertexte\|hyperliens]]. |

## La naissance d'Internet et le rôle de Xerox PARC

**Idée essentielle** : [[Internet]], le Web et l'[[Interface graphique|interface graphique]] ont des histoires liées, mais distinctes. [[ARPANET]] ouvre la voie aux réseaux informatiques à grande distance ; [[Xerox PARC]] développe l'[[Ordinateur personnel|ordinateur personnel]] connecté et le [[Réseau local|réseau local]] [[Ethernet]] ; le Web apparaît plus tard au [[CERN]].

Trois inventions à distinguer :

| Invention | À quoi sert-elle ? | Repère historique |
|---|---|---|
| [[ARPANET]] | Relier des ordinateurs situés dans différents centres de recherche | Premiers échanges entre UCLA et [[SRI International\|SRI]] en 1969 ; ancêtre majeur d'Internet |
| [[Ethernet]] | Relier des ordinateurs et des périphériques au sein d'un réseau local | Développé à Xerox PARC dans les années 1970 |
| [[World Wide Web]] | Consulter et relier des documents grâce aux [[Lien hypertexte\|liens hypertextes]] | Proposé par Tim Berners-Lee au CERN en 1989 |

Le passage aux [[Protocole de communication|protocoles]] TCP/IP ([[Suite des protocoles Internet]]) en 1983 permet à différents réseaux de communiquer selon des règles communes. Le Web est ensuite un **service construit sur Internet** : on peut donc avoir Internet sans le Web (le [[Courrier électronique|courriel]], le transfert de fichiers ou la [[Messagerie instantanée|messagerie]] en sont d'autres services).

## 2. Xerox PARC : imaginer l'ordinateur personnel connecté

Le Palo Alto Research Center, appelé [[Xerox PARC]], ne crée pas [[Internet]]. Ses chercheurs explorent toutefois une autre idée fondamentale : chaque personne pourrait disposer de **son propre ordinateur** ([[Ordinateur personnel]]), relié à d'autres ordinateurs et à des ressources partagées.

Conçu en **1973**, le **Xerox Alto** associe un écran graphique, un clavier, une [[Souris (informatique)|souris]] et une connexion réseau. Les chercheurs de PARC développent aussi **[[Ethernet]]**, qui relie les machines entre elles et permet de partager des ressources comme les [[Imprimante|imprimantes]]. C'est la vision d'une informatique **personnelle et distribuée** ([[Informatique distribuée]]).

Pour l'histoire du [[Design d'interaction|design d'interaction]], l'Alto est particulièrement important : l'ordinateur n'est plus seulement une machine à laquelle on donne des instructions spécialisées ([[Interface en ligne de commande]]). Son écran, sa souris, ses fenêtres et ses menus ([[WIMP]]) permettent d'**agir sur des éléments visibles** ([[Manipulation directe]]). Le réseau devient lui aussi une dimension du travail quotidien : échanger des informations, accéder à des ressources communes.

*Figure : le Xerox Alto, écran vertical au format d'une page, clavier, souris et unité centrale sous le bureau.*
![[2 - Histoire du design - p5.jpg]]

Xerox a fondé PARC en 1970. L'Alto n'a jamais été vendu au public (environ deux mille exemplaires, utilisés dans les laboratoires et les universités), mais il a fixé le modèle des interfaces à fenêtres, icônes, menus et pointeur ([[WIMP]]). La visite de Steve Jobs à PARC en 1979 a inspiré le Lisa (1983) puis le [[Macintosh]] (1984) d'[[Apple]]. Ethernet est décrit par Robert Metcalfe dans une note du 22 mai 1973, puis normalisé par l'[[IEEE]] (norme 802.3, 1983). PARC invente aussi l'[[Imprimante|imprimante laser]] (Gary Starkweather, 1971) et le langage Smalltalk, issu du projet de [[Dynabook]] d'Alan Kay. L'Alto rompt avec le modèle dominant de l'époque, l'[[Ordinateur central|ordinateur central]] partagé entre de nombreux utilisateurs en [[Temps partagé|temps partagé]], et ouvre la voie à l'[[Interaction homme-machine|interaction homme-machine]] graphique. [[Complément hors du cours|ⓘ]]

## 2 bis. De l'ARPANET au courrier électronique

Le support numérote deux sections « 2 ». Au début des années 1970, [[ARPANET]] est avant tout conçu comme une infrastructure de **partage de ressources informatiques**. Ses utilisateurs se mettent pourtant vite à l'employer pour **communiquer entre eux**.

Le succès est spectaculaire : selon le chapitre (celui de [[2 - De courrier à courriels]]), en **1974**, environ **trois quarts du trafic** d'ARPANET correspondent déjà à l'envoi de [[Courrier électronique|courriels]]. Les fonctions « **répondre** » et « **transférer** », intégrées par **John Vittal** (en 1975, dans son programme MSG, [[Client de messagerie]]), facilitent encore la circulation des messages.

Le courriel introduit plusieurs transformations essentielles :
- il réduit le **coût matériel** de la communication ;
- il **accélère** considérablement l'échange ([[Accélération sociale]]) ;
- il permet surtout une communication **asynchrone** ([[Communication asynchrone]]) : l'émetteur et le destinataire n'ont plus besoin d'être disponibles en même temps.

Conséquence : puisqu'un message est très facile à envoyer, on peut en envoyer beaucoup plus.

## La Silicon Valley

L'histoire de la [[Silicon Valley]] et d'[[Internet]] est liée à la transformation d'une région agricole de Californie en centre mondial de l'innovation technologique et du numérique.

**Les origines et le rôle de l'[[Université Stanford|université Stanford]] (1930-1950)**
- **Frederick Terman**, doyen (de l'école d'ingénieurs) de Stanford, encourage les étudiants à créer leurs propres entreprises technologiques locales ([[Start-up]]).
- **[[Hewlett-Packard]]** : William Hewlett et David Packard commencent à travailler en 1938 dans un garage de Palo Alto et fondent officiellement leur entreprise en janvier 1939, posant les bases de l'écosystème local. [[Erreurs du cours#^e-2-histoire-du-design|✎]]
- Le **[[Stanford Research Park]]** (d'abord nommé Stanford Industrial Park) est créé en 1951 pour louer des terres universitaires aux entreprises et rapprocher la recherche de l'industrie. [[Erreurs du cours#^e-2-histoire-du-design|✎]]

**L'ère des [[Semi-conducteur|semi-conducteurs]] et du silicium (1950-1970)**
- Le **silicium**, matériau de base des [[Transistor|transistors]] et des [[Circuit intégré|circuits intégrés]], donne son nom à la région ; l'expression « Silicon Valley » est popularisée par le journaliste Don Hoefler en 1971.
- **[[Intel]]**, fondée en 1968 à Mountain View (son siège s'installe ensuite à Santa Clara), révolutionne l'informatique avec le [[Processeur|microprocesseur]]. [[Erreurs du cours#^e-2-histoire-du-design|✎]]
- **[[ARPANET]]**, financé par le Pentagone ([[Département de la Défense des États-Unis]]), connecte dès la fin des années 1960 des centres de recherche universitaires, dont le [[SRI International|SRI]], situé dans la région.

Le transistor lui-même n'a pas été inventé dans la vallée, mais aux [[Laboratoires Bell|laboratoires Bell]] (New Jersey) en 1947. L'un de ses inventeurs, William Shockley, fonde en 1956 à Mountain View le Shockley Semiconductor Laboratory ; huit de ses ingénieurs le quittent en 1957 pour créer [[Fairchild Semiconductor]], dont sont issus Robert Noyce et Gordon Moore, fondateurs d'Intel. Le premier microprocesseur commercial, l'Intel 4004, date de 1971. Gordon Moore avait observé dès 1965 que le nombre de composants par circuit doublait à intervalle régulier ([[Loi de Moore]]). [[Complément hors du cours|ⓘ]]

Le modèle de la vallée repose aussi sur un mode de financement : le [[Capital-risque|capital-risque]], où des investisseurs apportent des fonds à de jeunes entreprises en échange d'une part de leur capital. Arthur Rock finance ainsi Fairchild (1957) puis Intel (1968), et les fonds s'installent dans les années 1970 sur Sand Hill Road, à Menlo Park, près de Stanford. Universités, crédits militaires et capital-risque forment le triangle souvent cité pour expliquer l'essor de la région. [[Complément hors du cours|ⓘ]]

## 3. Le Web : accéder aux documents par des liens

En **1989**, au **[[CERN]]**, Tim Berners-Lee propose le [[World Wide Web]] pour faciliter le partage d'informations entre scientifiques. Le Web rend possible la **navigation entre des documents reliés par des liens** ([[Lien hypertexte]]). Son logiciel est diffusé en 1991. Il ne faut pas confondre la naissance du Web avec celle d'[[Internet]], dont les réseaux existaient déjà.

**Objectif initial** : créer un système d'information mondial fondé sur l'hypertexte, pour relier et échanger des données entre chercheurs du monde entier.

**Dates importantes**
- **Mars 1989** : première proposition, « Information Management: A Proposal ».
- **1990** : premier [[Navigateur web|navigateur]] (WorldWideWeb) et premier [[Serveur web|serveur web]], sur un ordinateur [[NeXT]], par Tim Berners-Lee avec l'aide de Robert Cailliau.
- **1993** : le CERN place le logiciel du Web dans le [[Domaine public|domaine public]], gratuit et ouvert à tous.

Le premier site web, info.cern.ch, est mis en ligne fin 1990 au CERN, et le CERN publie son ouverture du logiciel le 30 avril 1993. Berners-Lee fonde en 1994, au [[Massachusetts Institute of Technology|MIT]], le [[W3C]] (*World Wide Web Consortium*), qui normalise depuis les technologies du Web. [[Complément hors du cours|ⓘ]]

## Fiche de lecture : « Du réseau informatique au World Wide Web »

Pages 9 à 17 : résumé d'un chapitre 2 d'un ouvrage dont le support ne donne ni le titre ni l'auteur (« l'auteur »).

### 1. Idée générale du chapitre

[[Internet]] existe **avant** le Web, mais il reste longtemps difficile d'accès, abstrait et réservé à des utilisateurs capables de comprendre son fonctionnement technique. Au début des années 1990, Internet est encore surtout une **infrastructure** qui fait communiquer des ordinateurs grâce à des [[Protocole de communication|protocoles]] communs, notamment TCP/IP ([[Suite des protocoles Internet]]). Pour devenir un espace culturel et social accessible au grand public, **il lui manque une interface**.

L'auteur résume : Internet doit devenir **intelligible à tout un chacun**. Il lui faut l'équivalent de ce que les fenêtres ([[WIMP]]), la [[Souris (informatique)|souris]] et l'[[Interface graphique|interface graphique]] ont été pour l'[[Ordinateur personnel|ordinateur personnel]]. Le [[World Wide Web]] va remplir cette fonction.

Le chapitre ne fait pas une histoire seulement technique : il en propose une lecture **politique et culturelle**. Au moment où le Web apparaît se rencontrent plusieurs traditions : [[Contre-culture|contre-culture]] américaine, [[Libertarianisme|libertarianisme]], culture entrepreneuriale ([[Entrepreneuriat]]) de la [[Silicon Valley]], croyance dans l'émancipation par la technologie et imaginaire [[Cybernétique|cybernétique]].

### 2. Une distinction fondamentale : Internet ≠ Web

- **[[Internet]]** désigne d'abord le **[[Réseau|réseau]]**, l'infrastructure qui permet la communication entre ordinateurs. À ce stade, ce n'est guère plus que la connexion physique des ordinateurs, l'adoption de [[Protocole de communication|protocoles communs]] (notamment TCP/IP), une « langue commune » qui permet aux machines d'échanger des données.
- **Le Web** ([[World Wide Web]]) est une **couche** qui vient s'ajouter à Internet. Son rôle est déterminant : il rend les ressources du réseau accessibles à des personnes qui ne maîtrisent pas les protocoles informatiques sous-jacents.

En résumé : **Internet = infrastructure de communication** ; **Web = système pour organiser, relier, consulter et publier des documents sur cette infrastructure**. Pour une histoire du [[Design d'interaction|design de l'interaction]], la distinction est essentielle : le réseau existait déjà, mais c'est en grande partie **l'interface** qui permet son appropriation sociale.

Dans le vocabulaire des réseaux, le Web est une application de la couche la plus haute, qui s'appuie sur le transport (TCP) et l'adressage (IP, [[Adressage IPv4 et CIDR]]) d'Internet ; voir [[Modèle OSI]] et [[Suite des protocoles Internet]]. [[Complément hors du cours|ⓘ]]

### 3. Avant le Web : comment imaginer Internet ?

Avant que le Web n'en donne une représentation concrète, de nombreuses **[[Métaphore|métaphores]]** servent à expliquer [[Internet]] :

| Métaphore | Ce qu'elle suggère |
|---|---|
| Infobahn | [[Autoroute de l'information\|autoroute de l'information]] |
| Toile | [[Réseau\|réseau]] de connexions |
| Bibliothèque | accès à la connaissance |
| Place du village | espace social ([[Sociabilité\|sociabilité]]) |
| [[Cyberespace]] | espace numérique parallèle |
| Matrice | univers informationnel |
| [[Métavers]] | espace virtuel habitable |

Ces métaphores montrent une difficulté : comment représenter quelque chose qui n'a pas encore de forme perceptible ? Le grand public reste largement perplexe devant ce nouvel espace. La question intéresse directement le design : **comment donner une forme sensible, compréhensible et manipulable à une infrastructure invisible ?** Le Web peut être vu comme une réponse à ce problème.

### 4. Le Web comme « cheval de Troie »

Formule de l'auteur : « Internet a besoin d'un cheval de Troie. Ce cheval de Troie s'appellera le World Wide Web. » Le [[World Wide Web|Web]] va permettre à [[Internet]] :
- d'entrer dans les foyers ;
- d'attirer des utilisateurs non spécialistes ;
- de devenir un espace culturel ;
- de devenir un espace économique ;
- de devenir peu à peu une infrastructure de la vie quotidienne.

Le Web est donc une **interface de démocratisation** du réseau ; mais cette démocratisation entraîne aussi sa **commercialisation** ([[Bulle Internet]]).

### 5. La « Californian Ideology »

L'auteur situe l'apparition du Web dans un contexte idéologique : au début des années 1990 se cristallise une idéologie de la [[Silicon Valley]] articulée autour de plusieurs traditions ([[Idéologie californienne]]).

- **Héritage de la [[Contre-culture|contre-culture]]** : une partie de la culture informatique américaine hérite des idéaux des [[Mouvement hippie|mouvements hippies]] et communautaires : défiance envers les institutions, autonomie individuelle, organisation horizontale ([[Réseau décentralisé]]), circulation libre de l'information, émancipation personnelle.
- **[[Libertarianisme]]** : une philosophie politique qui valorise fortement l'individu, la propriété, l'initiative privée, le marché, la limitation de l'intervention de l'État.
- **Culture entrepreneuriale** ([[Entrepreneuriat]]) : ces valeurs rencontrent l'esprit d'entreprise de la Silicon Valley. L'auteur décrit une fusion entre la défiance envers l'appareil gouvernemental et l'entrepreneuriat technologique.

Le résultat est paradoxal : des idéaux d'émancipation issus de la contre-culture sont peu à peu intégrés à une économie technologique libérale ([[Libéralisme économique]]).

L'expression vient d'un essai de deux chercheurs britanniques, Richard Barbrook et Andy Cameron, « The Californian Ideology » (1995), qui critique ce mélange de bohème hippie et de [[Libéralisme économique|libéralisme économique]]. L'historien Fred Turner a retracé ce passage de la contre-culture à la cyberculture, autour de Stewart Brand et du *[[Whole Earth Catalog]]*, dans *[[Aux sources de l'utopie numérique]]* (2006) ; Brand coorganise d'ailleurs en 1984 la première Hackers Conference, qui célèbre l'[[Éthique hacker|éthique hacker]]. [[Complément hors du cours|ⓘ]]

### 6. Ayn Rand et l'individualisme libertarien

L'auteur accorde une place importante à **Ayn Rand**, référence intellectuelle majeure d'une partie du mouvement libertarien américain ([[Libertarianisme]]). Dans la logique du chapitre, l'individu doit pouvoir poursuivre librement ses intérêts, avec le moins possible d'intervention de l'État. L'auteur associe cette philosophie à la transformation de la culture technologique américaine : la technologie n'est plus seulement un outil collectif ou scientifique, mais un **instrument d'autonomie et d'augmentation des capacités individuelles**.

Le chapitre relie Ayn Rand à **Alan Greenspan**, membre de son entourage dans sa jeunesse, devenu ensuite président de la [[Réserve fédérale]] américaine ([[Banque centrale|banque centrale]] des États-Unis) : le libertarianisme n'est pas resté marginal, il a pénétré les institutions économiques américaines.

Ayn Rand (1905-1982), romancière et philosophe américaine née en Russie, défend l'« [[Objectivisme|objectivisme]] » : l'égoïsme rationnel comme morale et le [[Capitalisme|capitalisme]] sans entrave comme seul système juste, notamment dans *[[La Grève (roman)|La Grève]]* (*Atlas Shrugged*, 1957). Greenspan a présidé la Réserve fédérale de 1987 à 2006. [[Complément hors du cours|ⓘ]]

### 7. Les trois grandes idées de la cyberculture

1. **L'individualisme libertarien** ([[Libertarianisme]]) : la technologie doit renforcer l'autonomie individuelle.
2. **L'émancipation du corps par la technologie** : la technologie permettrait à l'esprit de dépasser certaines contraintes physiques. Cette idée revient dans les imaginaires du [[Cyberespace|cyberespace]], de la [[Réalité virtuelle|réalité virtuelle]], des [[Avatar (informatique)|avatars]] et du [[Métavers|métavers]] (voir aussi [[Transhumanisme]]).
3. **Une société [[Cybernétique|cybernétique]] interconnectée** : l'interconnexion des individus pourrait produire une nouvelle forme d'organisation sociale globale.

L'auteur résume cette vision comme la rencontre d'une conception politique et économique libertarienne, d'une éthique de l'être humain augmenté par la technologie et de la vision d'une société mondialisée ([[Mondialisation]]) équilibrée par l'interconnexion cybernétique.

### 8. Un paradoxe : le Web naît dans une institution publique

Alors que l'imaginaire libertarien ([[Libertarianisme]]) se méfie de l'État et des institutions, le Web naît dans une institution scientifique publique, le **[[CERN]]** (sigle de l'ancien Conseil européen pour la recherche nucléaire, aujourd'hui Organisation européenne pour la recherche nucléaire). L'auteur souligne volontairement cette contradiction : [[Internet]] est présenté comme l'héritier de la recherche militaire américaine ([[DARPA]]), le Web naît dans un centre européen de recherche scientifique. [[Erreurs du cours#^e-2-histoire-du-design|✎]]

Le personnage central est **Tim Berners-Lee** : avec **Robert Cailliau**, il développe au CERN le système qui deviendra le [[World Wide Web]]. Le Web permet de consulter une toile de documents hypertextes ([[Lien hypertexte]]) à travers une architecture [[Modèle client-serveur|client-serveur]].

### 9. Les trois technologies fondamentales du Web

**[[URL]] (*Uniform Resource Locator*)** : donne une adresse identifiable à une ressource. Au lieu de manipuler directement des [[Adressage IPv4 et CIDR|adresses IP]] complexes, l'utilisateur accède aux ressources par des adresses composées de mots (exemple du texte : `www.wikipedia.org`, voir [[Encyclopédie]]).

En termes de [[Design d'interaction|design d'interaction]], l'URL transforme une infrastructure technique abstraite en **espace adressable** : une ressource possède désormais une « adresse ». On retrouve une [[Métaphore|métaphore]] spatiale (adresse → lieu → navigation → site → page) : le vocabulaire même du Web transforme le réseau en espace.

C'est en réalité le [[DNS]] (*Domain Name System*, 1983) qui traduit un [[Nom de domaine|nom de domaine]] comme `www.wikipedia.org` en adresse IP ; l'URL l'intègre dans une adresse complète qui précise aussi le protocole et le chemin de la ressource : `https://fr.wikipedia.org/wiki/World_Wide_Web` (protocole `https`, nom d'hôte `fr.wikipedia.org`, chemin `/wiki/World_Wide_Web`). [[Complément hors du cours|ⓘ]]

### 10. HTTP : communiquer entre navigateur et serveur

**[[HTTP]] (*HyperText Transfer Protocol*)** organise les requêtes entre un utilisateur et un [[Serveur web|serveur]]. Exemples du texte :
- `GET` : récupérer des données ;
- `POST` : envoyer des données ;
- `DELETE` : supprimer des données.

Schéma :

```
UTILISATEUR
   ↓
NAVIGATEUR
   ↓ requête HTTP
INTERNET
   ↓
SERVEUR
   ↓ réponse
NAVIGATEUR
   ↓
PAGE AFFICHÉE
```

Ce système [[Modèle client-serveur|client-serveur]] reste l'un des principes fondamentaux du Web.

La première version de HTTP (1991) ne connaissait que `GET` ; `POST` et les autres méthodes arrivent avec HTTP/1.0 (1996) et HTTP/1.1 (1997). La réponse du serveur commence par un [[Code d'état HTTP|code d'état]] : `200` (succès), `404` (ressource introuvable), `500` (erreur du serveur). HTTPS est la version [[Chiffrement|chiffrée]] de HTTP. [[Complément hors du cours|ⓘ]]

### 11. HTML : donner une structure à l'information

**[[HTML]] (*HyperText Markup Language*)** structure l'information d'une page Web : texte, titres, paragraphes, images, liens, différentes ressources. Mais l'innovation essentielle est le **[[Lien hypertexte|lien hypertexte]]** : il permet de passer d'une information à une autre par un simple clic. C'est une transformation majeure du rapport au savoir : la lecture n'est plus nécessairement `début → milieu → fin`, elle peut devenir `page → lien → page → lien → autre ressource`. La navigation devient **non linéaire**.

HTML est un [[Langage de balisage|langage de balisage]] : chaque élément est encadré par des balises, par exemple `<h1>Titre</h1>`, `<p>Un paragraphe</p>`, et un lien s'écrit `<a href="https://home.cern">le site du CERN</a>`. [[Complément hors du cours|ⓘ]]

### 12. Le lien hypertexte comme geste de design

Le [[Lien hypertexte|lien hypertexte]] transforme une opération informatique complexe en une interaction extrêmement simple : **voir → pointer → cliquer → accéder** ([[Manipulation directe]]). Le réseau devient manipulable : l'utilisateur n'a plus besoin de comprendre la structure informatique du réseau pour l'utiliser. C'est une caractéristique fondamentale du [[Design d'interface|design d'interface]] : **cacher la complexité technique derrière une action compréhensible**. Le clic devient une sorte de geste élémentaire du [[Cyberespace|cyberespace]].

L'idée d'hypertexte précède le Web : Vannevar Bush imagine en 1945 le [[Memex]], une machine à associer des documents ; Ted Nelson invente le mot « hypertexte » en 1965 ; Douglas Engelbart montre en 1968, au [[SRI International|SRI]], des liens cliquables à la souris ([[Démonstration d'Engelbart]]). [[Complément hors du cours|ⓘ]]

### 13. 1993 : rendre le Web librement accessible

Le texte insiste sur une décision : en 1993, Berners-Lee convainc le [[CERN]] de rendre librement disponibles le [[Code source|code source]] du [[Navigateur web|navigateur]], le code du [[Serveur web|serveur]] et les spécifications des [[Protocole de communication|protocoles]] du Web. Cette décision permet au Web de se diffuser ([[Domaine public]]).

L'auteur compare cette transformation à celle du **[[Macintosh]] en 1984** ([[Apple]]) : de même que l'[[Interface graphique|interface graphique]] avait contribué à transformer l'ordinateur en [[Ordinateur personnel|ordinateur personnel]], le Web transforme [[Internet]] en un espace accessible au grand public. C'est un moment essentiel de l'histoire du design numérique.

La décision tombe au bon moment : la même année, l'université du Minnesota annonce qu'elle fera payer certaines utilisations de Gopher, un système concurrent de consultation de documents en ligne, ce qui détourne une partie des développeurs vers le Web, libre et gratuit. Cette logique d'ouverture est proche de celle du [[Logiciel libre|logiciel libre]], dont le mouvement est né en 1983, et fait du Web un des grands [[Communs numériques|communs numériques]]. [[Complément hors du cours|ⓘ]]

### 14. Une transformation sensorielle d'Internet

- **Avant le Web** : [[Internet]] = lignes de commande ([[Interface en ligne de commande]]) + [[Protocole de communication|protocoles]] + échange entre machines.
- **Après le Web** : Internet devient **visible**. L'auteur écrit que le [[Cyberespace|cyberespace]] devient un « univers visuel » où chacun peut lire et publier des contenus organisés dans des fenêtres ([[WIMP]]).

On peut parler d'une transformation : abstraite → visuelle ; experte → grand public ; technique → sensorielle ; machine → interface ([[Interface graphique]]).

### 15. Mosaic : rendre le Web graphique

Deuxième étape : le **[[Navigateur web|navigateur]] Mosaic**, développé au NCSA, qui permet d'intégrer dans les pages des **images** et des **[[Formulaire web|formulaires interactifs]]**. Cela paraît banal aujourd'hui, mais c'est décisif : le Web n'est plus seulement un système pour consulter du texte relié par des liens ([[Lien hypertexte]]), il devient un **média graphique**.

*Figure : page d'accueil de NCSA Mosaic pour [[Microsoft]] Windows, avec barre d'outils, champ d'adresse et logo en image.*
![[2 - Histoire du design - p16.jpg]]

Mosaic est sorti en 1993 au NCSA (*National Center for Supercomputing Applications*, université de l'Illinois), écrit notamment par Marc Andreessen et Eric Bina ; il affichait les images dans le texte même de la page, et non dans une fenêtre séparée. [[Complément hors du cours|ⓘ]]

### 16. Marc Andreessen et Netscape

Marc Andreessen, l'un des développeurs de Mosaic, quitte le monde universitaire pour créer une entreprise ([[Start-up]]), qui développe **Netscape** ([[Navigateur web]]). Le navigateur devient l'un des symboles du premier Web commercial. Le nom de code interne du projet était **[[Mozilla]]**, contraction de « Mosaic Killer ». Ce passage marque un basculement : recherche universitaire → entreprise ([[Entrepreneuriat]]) ; expérimentation → industrie ; outil scientifique → marché.

Netscape (fondée en 1994) entre en bourse en 1995 ([[Introduction en bourse]]) : son action presque doublée dès le premier jour annonce la [[Bulle Internet|bulle Internet]] sur les [[Marché financier|marchés boursiers]], qui éclate en 2000. La « [[Guerre des navigateurs|guerre des navigateurs]] » l'oppose ensuite à Internet Explorer de [[Microsoft]]. Le mot Mozilla mêle aussi « Mosaic » et « Godzilla ». Le code de Netscape, ouvert en 1998 ([[Logiciel libre]] ; l'expression « open source », voir [[Licences libres]], est forgée la même année), a donné le projet Mozilla et le navigateur Firefox (2004), dont le logo figure sur la page du support. [[Complément hors du cours|ⓘ]]

### 17. De l'autoroute à la toile

Le chapitre revient sur une **bataille de [[Métaphore|métaphores]]**. Bill Gates ([[Microsoft]]) utilise l'image de l'**[[Autoroute de l'information|autoroute de l'information]]**, qui suggère des voies, des infrastructures, des accès, des règles et potentiellement des péages. À l'inverse, *Macworld* propose en 1995 de voir [[Internet]] comme une sorte d'**[[Encyclopédie|encyclopédie]]** : illimitée, graphique, sociale, connectée à l'espace marchand.

Cette opposition compte, car **les métaphores influencent la manière dont une technologie est comprise** :
- autoroute → circulation ;
- bibliothèque → connaissance ;
- place du village → [[Sociabilité|sociabilité]] ;
- toile → connexion ;
- [[Cyberespace|cyberespace]] → territoire.

Le design du numérique repose donc aussi sur une construction imaginaire et linguistique (voir [[Imaginaire]]).

L'expression *information superhighway* a surtout été popularisée par Al Gore, sénateur puis vice-président des États-Unis, au début des années 1990. [[Complément hors du cours|ⓘ]]

## Grande chronologie

| Date | Événement | Portée |
|---|---|---|
| 1932 | Aldous Huxley publie *[[Le Meilleur des mondes]]* | Société contrôlée par le conditionnement et le plaisir ([[Dystopie\|dystopie]]) |
| 1939-1945 | [[Seconde Guerre mondiale]] | Accélération des recherches sur [[Radar\|radar]], calcul, communication, automatisation |
| Années 1940 | Travaux de Norbert Wiener | Concepts qui structurent la [[Cybernétique\|cybernétique]] |
| 1942-1953 | [[Conférences Macy]] | Diffusion interdisciplinaire des notions de [[Signal (télécommunications)\|signal]], [[Information\|information]], communication, [[Rétroaction\|rétroaction]] |
| 1949 | George Orwell publie *[[1984 (roman)\|1984]]* | Imaginaire du [[Totalitarisme\|totalitarisme]], de la [[Surveillance de masse\|surveillance]], du contrôle politique |
| Années 1950 | [[Beat Generation]] | Kerouac, Ginsberg, Cassady, Burroughs |
| 1954 | Huxley publie *[[Les Portes de la perception]]* | Perception, conscience, substances psychédéliques |
| 1959 | William Burroughs publie *[[Le Festin nu]]* | Contrôle, surveillance, manipulation |
| Années 1960 | Contre-culture hippie ([[Mouvement hippie]]) | Communautés alternatives, [[Psychédélisme\|psychédélisme]], critique des institutions |
| Années 1970 | Rencontre croissante entre [[Contre-culture\|contre-culture]], ingénieurs, informatique et [[Silicon Valley]] | |
| 1982 | Sortie de *[[Tron]]* | Univers informatique représenté comme espace habitable |
| 1984 | Commercialisation du [[Macintosh]] ([[Apple]]) | Informatique personnelle à [[Interface graphique\|interface graphique]] |
| 1984 | William Gibson publie *[[Neuromancer\|Neuromancien]]* | Popularisation du [[Cyberespace\|cyberespace]], imaginaire [[Cyberpunk\|cyberpunk]] ([[Science-fiction\|science-fiction]]) |

Les dix conférences Macy consacrées à la cybernétique se tiennent de 1946 à 1953 ; la date 1942 renvoie à une réunion préparatoire de la fondation Macy. [[Complément hors du cours|ⓘ]]

Les deux lignes de 1984 se rejoignent : le Macintosh est lancé par un spot publicitaire réalisé par Ridley Scott et diffusé en janvier 1984, où une athlète brise l'écran d'un orateur à la manière du [[Big Brother]] de *1984* ; l'informatique personnelle s'y présente comme une arme contre le conformisme et le contrôle, un thème hérité de la contre-culture. [[Complément hors du cours|ⓘ]]

## Personnages et concepts à retenir

**Personnages**
- **Norbert Wiener** : [[Cybernétique|cybernétique]], [[Information|information]], [[Rétroaction|rétroaction]], [[Contrôle (cybernétique)|contrôle]].
- **Jack Kerouac** : [[Beat Generation]], voyage, liberté, refus du conformisme.
- **Allen Ginsberg** : Beat Generation et [[Contre-culture|contre-culture]].
- **William S. Burroughs** : contrôle, [[Surveillance de masse|surveillance]], manipulation ([[Le Festin nu]]).
- **Neal Cassady** : figure de transmission entre Beat Generation et hippies ([[Mouvement hippie]]).
- **Aldous Huxley** : perception, [[Psychédélisme|psychédélisme]], contrôle social ([[Le Meilleur des mondes]]).
- **George Orwell** : surveillance, État totalitaire ([[Totalitarisme]]), contrôle politique ([[1984 (roman)|1984]]).
- **Edward Bernays** : [[Propagande|propagande]] et manipulation de l'opinion (voir [[Fabrique du consentement]]).
- **Philip K. Dick** : doute sur la réalité, perception, manipulation ([[Science-fiction]]).
- **William Gibson** : [[Cyberespace|cyberespace]], [[Cyberpunk|cyberpunk]], réseaux numériques ([[Neuromancer]]).

Le philosophe Gilles Deleuze emprunte à Burroughs le mot « contrôle » pour décrire, dans son « Post-scriptum sur les sociétés de contrôle » (1990), les [[Société de contrôle|sociétés de contrôle]], qui succèdent selon lui aux sociétés disciplinaires analysées par Michel Foucault ([[Panoptique]]). Le film *[[Blade Runner]]* (Ridley Scott, 1982) adapte un roman de Philip K. Dick, *Les androïdes rêvent-ils de moutons électriques ?* (1968). [[Complément hors du cours|ⓘ]]

**Concepts essentiels** (le titre de la page garde un numéro « XXXIV » sans suite)

| Concept | Définition du support |
|---|---|
| [[Cybernétique]] | Étude des mécanismes de communication et de contrôle dans les [[Système complexe\|systèmes complexes]] |
| [[Information]] | Élément qui permet au système d'observer son environnement et d'adapter son comportement |
| [[Rétroaction]] (*feedback*) | Retour d'information qui permet à un système de modifier son action |
| [[Homéostasie]] | Maintien dynamique de l'équilibre d'un système |
| [[Contrôle (cybernétique)\|Contrôle]] | Capacité à orienter ou modifier le comportement d'un système |
| [[Réseau]] | Organisation composée d'éléments reliés les uns aux autres |
| [[Réseau décentralisé\|Décentralisation]] | Organisation dont le fonctionnement ne dépend pas nécessairement d'un centre unique |
| [[Contre-culture]] | Ensemble de mouvements contestant les valeurs dominantes d'une société |
| [[Cyberespace]] | Représentation du réseau informatique comme un espace virtuel navigable |
| [[Cyberpunk]] | Genre culturel associant haute technologie, réseaux numériques, domination économique et sociétés souvent dystopiques |

## Diapositives illustrées

**1995 : le coup d'envoi de l'Internet grand public** (photo d'un modem U.S. Robotics 56K Faxmodem). Le support situe en 1995 l'arrivée du [[Modem|modem]] 56k dans les foyers américains ; les modems 56k ne sont commercialisés qu'à partir de 1997 (normes concurrentes x2 et K56flex, puis norme commune V.90 de l'[[Union internationale des télécommunications|UIT]] en 1998), et le grand public de 1995 se connecte plutôt à 14,4 ou 28,8 kbit/s ([[Débit binaire]]). [[Erreurs du cours#^e-2-histoire-du-design|✎]] C'est le coup d'envoi de l'[[Internet]] grand public : le Web ([[World Wide Web]]), inventé par Tim Berners-Lee, devient accessible à des millions d'utilisateurs. « Surfer sur internet » est une expression nouvelle et excitante, mais l'activité reste surtout l'apanage des informaticiens et des *[[Geek|geeks]]*.

**Messageries et chats.** ICQ (1996) et IRC (1988) popularisent la communication instantanée en ligne ; ce ne sont pas les premières expériences du genre, déjà possibles dans les années 1970 (Talkomatic sur le système [[PLATO (système)|PLATO]] en 1973, commande `talk` des systèmes [[Unix]]). [[Erreurs du cours#^e-2-histoire-du-design|✎]] Voir [[Messagerie instantanée]].

*Figure : fenêtres du client IRC mIRC (2001) : liste de canaux à gauche, conversations et liste des participants.*
![[2 - Histoire du design - p21.jpg]]

**[[Portail web|Portails web]].** AltaVista, Yahoo, GeoCities et Lycos précèdent [[Google]] comme points d'entrée du Web ; seul Yahoo est à l'origine un répertoire de sites classés par thèmes et « gérés à la main par des humains » ([[Annuaire web]]), AltaVista et Lycos sont des [[Moteur de recherche|moteurs de recherche]] qui indexent le Web par des robots ([[Robot d'indexation]]), et GeoCities est un hébergeur de pages personnelles ([[Hébergement web]]). [[Erreurs du cours#^e-2-histoire-du-design|✎]] Ces portails deviennent des points d'entrée incontournables pour naviguer sur le Web.

*Figure : page d'accueil d'AltaVista dans Netscape ([[Navigateur web]]), octobre 1999 : champ de recherche, chaînes thématiques et répertoire.*
![[2 - Histoire du design - p22.jpg]]

Google (1998) s'impose en classant les pages selon les liens qu'elles reçoivent (algorithme [[PageRank]]) plutôt que par un répertoire tenu à la main. [[Complément hors du cours|ⓘ]]

**Menlo Park et la région de Stanford** (photo d'un ingénieur devant un ordinateur à [[Bande magnétique|bandes magnétiques]], datée de 1960 par le support). Cet écosystème rassemble ingénieurs, instituts de recherche et entreprises comme le Stanford Research Institute ([[SRI International]], installé à Menlo Park) et, à partir de 1970, le centre de recherche de Xerox à Palo Alto ([[Xerox PARC]]). [[Erreurs du cours#^e-2-histoire-du-design|✎]] **Avancées technologiques** : la [[Souris (informatique)|souris]], les [[Ordinateur personnel|ordinateurs personnels]] et [[Ordinateur portable|portables]], ainsi qu'[[ARPANET]] y sont développés, en collaboration avec des projets militaires ([[Département de la Défense des États-Unis]]).

La souris est mise au point au SRI par l'équipe de Douglas Engelbart (brevet déposé en 1967, démonstration publique en 1968, [[Démonstration d'Engelbart]]) ; le portable reste à PARC un concept, le [[Dynabook]] d'Alan Kay (1972) ; ARPANET est conçu par l'ARPA ([[DARPA]]) et construit surtout par [[BBN]] à Cambridge (Massachusetts), le SRI en étant le deuxième nœud. [[Complément hors du cours|ⓘ]]

**La [[Cybernétique|cybernétique]] et la [[Théorie de l'information|théorie de l'information]]** structurent l'évolution des technologies en posant les bases d'un [[Réseau|réseau]] global d'échange d'[[Information|informations]]. **Une influence hippie et émancipatrice** : paradoxalement, l'[[Internet]] moderne naît aussi d'un esprit contre-culturel ([[Contre-culture]]) ; les années 1960 voient émerger un mouvement alternatif ([[Mouvement hippie]]) qui marie technologie et idéaux de transformation sociale. (L'illustration montre deux chercheurs aux cheveux longs devant des ordinateurs des années 1970.)

**Stewart Brand et le *[[Whole Earth Catalog]]*.** Lancé en 1968, ce catalogue devient une sorte de bible pour les informaticiens de Menlo Park. [[Erreurs du cours#^e-2-histoire-du-design|✎]] Il propose des pièces électroniques en [[Vente par correspondance|vente par correspondance]], mais aussi des textes sur la [[Théorie de l'information|théorie de l'information]], et prône un usage libérateur de la technologie. Pour ces pionniers, [[Internet]] doit servir à échanger le savoir et permettre à chacun de s'émanciper : la technologie n'est pas seulement un outil, mais un vecteur de transformation sociale et personnelle.

*Figure : couverture du Whole Earth Catalog de l'automne 1970, sous-titré « access to tools », avec une photographie de la Terre vue de l'espace.*
![[2 - Histoire du design - p25.jpg]]

Le catalogue ne vendait rien lui-même : il recensait et commentait des outils, des livres et du matériel, avec l'adresse où se les procurer. Sa dernière édition (1974) porte en quatrième de couverture la formule « Stay hungry. Stay foolish. », que Steve Jobs ([[Apple]]) a reprise dans son discours de Stanford ([[Université Stanford]]) en 2005. [[Complément hors du cours|ⓘ]]

## Fiche de lecture : « La tragédie de la communication »

Pages 26 à 38 : résumé du chapitre dont le texte est scanné dans [[2 - De courrier à courriels]] (le détail, les exemples et les citations y sont). La fiche l'intitule « Chapitre 2 », et numérote ses sections de 1 à 13 sans section 2 ni 12.

1. **Idée générale.** Le chapitre retrace la transformation de nos manières de communiquer, du [[Courrier électronique|courrier électronique]] aux [[SMS]] et aux [[Réseau social|réseaux sociaux]]. Les technologies numériques n'ont pas seulement rendu la communication plus rapide : elles ont imposé une logique d'**efficacité ([[Raison instrumentale]]), de compression ([[Compression de données]]) et d'immédiateté** aux échanges humains. Mouvement double : nous communiquons davantage et plus facilement, mais cette abondance pousse à raccourcir les messages, simplifier le langage, supprimer les politesses ([[Savoir-vivre]]), accélérer la lecture. Une logique technique (optimiser la circulation de l'[[Information|information]] dans un [[Réseau|réseau]]) devient une **[[Norme sociale|norme sociale]]**.
2. **Une nouvelle conception de la communication** (section 3). Au début, la rapidité du [[Courrier électronique|courriel]] est un avantage pour les chercheurs et informaticiens. Les conventions (salutations, formules de politesse, relecture, préparation minutieuse) deviennent des obstacles. La communication est pensée en termes de **productivité** ([[Impératif de productivité]]) : communiquer efficacement, c'est aller directement à l'essentiel. Cette logique d'ingénieurs devient une norme générale.
3. **Le courriel imite d'abord la lettre** (section 4). Selon Marshall McLuhan ([[Le médium est le message]]), un nouveau média est d'abord utilisé comme celui qui le précède. Les premiers courriels reprennent les codes de la [[Correspondance épistolaire|correspondance]] : adresse, brouillon, signature, structure épistolaire, et des icônes ([[WIMP]]) empruntées à la poste ([[Poste (service postal)]]) : enveloppes, timbres ([[Timbre-poste]]), crayons ([[Skeuomorphisme]]). Selon John Vittal, ces parallèles aidaient les utilisateurs à comprendre le nouveau média. Phase de transition : lettre → courrier électronique → formes spécifiquement numériques.
4. **L'abondance des messages transforme l'écriture** (section 5). Quand les courriels se multiplient, il devient difficile de consacrer du temps à chacun ; la communication devient une succession de **transactions informationnelles** à traiter au plus vite ([[Analyse coût-bénéfice]]). Le journaliste Nick Bilton veut supprimer les « gentillesses » chronophages ; des lecteurs attachés aux correspondances longues le critiquent.
5. **La disparition progressive de la lettre** (section 6). Écrire une lettre fut longtemps un privilège ([[Alphabétisation]]). La démocratisation postale du XIXe siècle ([[Uniform Penny Post]]) fait exploser le nombre de lettres : aux États-Unis, 27 millions en 1840, 161 millions en 1860. Avec le courriel, la dynamique s'inverse : le nombre de lettres envoyées par des particuliers aurait baissé d'environ 70 % entre 2001 et 2020 aux États-Unis.
6. **Adorno** (section 7). Theodor W. Adorno, *[[Minima Moralia]]* (1951) : les principes de la logique économique et industrielle pénètrent la vie quotidienne ([[Rationalisation]]). Si « le temps, c'est de l'argent », économiser du temps devient une valeur en soi ; pourquoi écrire longuement quand une phrase suffit ? Adorno redoute que l'écriture personnelle soit remplacée par une communication abrupte, inspirée du langage administratif. L'optimisation ne concerne plus seulement les machines : elle transforme les comportements humains ([[Raison instrumentale]], [[École de Francfort]]).
7. **« Le code des enfants »** (section 8). Deuxième transformation : la [[Messagerie instantanée|messagerie instantanée]]. À partir de la fin des années 1990, les adolescents ([[Génération Y]]) utilisent ICQ et AOL Instant Messenger (AIM, [[AOL]]), conversent avec plusieurs personnes à la fois, d'une fenêtre à l'autre : la communication devient plus **fragmentée** et plus **continue**. Ils ne reproduisent plus les conventions de la lettre ([[Correspondance épistolaire]]) et inventent une écriture adaptée à l'écran.
8. **Une écriture hybride** (section 9) : suppression de lettres, homophones, acronymes (« lol », « stp »), ponctuation expressive, répétition des lettres, majuscules, ellipses, émoticônes ([[Langage SMS]]). Pour l'auteur, ce n'est pas une simple dégradation, mais un **nouveau code** adapté au média ; Pamela Takayoshi et Christina Haas montrent que la messagerie instantanée a ses propres règles ([[Sociolinguistique]]). La frontière s'estompe entre écriture, parole et image ([[Logogramme]]).
9. **Claude Shannon et la compression** (section 10). Shannon ([[Théorie de l'information]]) cherchait à optimiser la transmission de l'information. Avec la messagerie instantanée, **ce sont les humains qui compressent l'information** ([[Compression de données]]) : abréviations et simplifications réduisent le temps d'écriture et de lecture ([[Redondance (théorie de l'information)]]). La compression devient technique → linguistique → comportementale.
10. **Une transformation de la lecture** (section 11). Quand plusieurs fenêtres réclament l'attention ([[Économie de l'attention]]), la lecture linéaire devient trop lente ; le texte doit se comprendre presque instantanément ([[Charge cognitive]]). Selon Lieke Verheijen, il s'agit de parcourir le message le plus vite possible, quitte à négliger des règles linguistiques. On passe de *lire → comprendre → réfléchir* à *voir → reconnaître → répondre* (la fiche précise que cette dernière formule est sa propre synthèse du raisonnement du chapitre).
11. **Le SMS amplifie cette logique** (section 13). Dans les années 2000, le téléphone portable ([[Téléphone mobile]]) remplace l'ordinateur comme outil de communication des jeunes. Le format renforce les contraintes : petit écran, clavier réduit, limite historique de **160 caractères** ([[SMS]], [[GSM]]). En 2010, plus de 2 000 milliards de SMS auraient été envoyés chaque année aux États-Unis, les jeunes en envoyant et recevant une centaine par jour.

**Références théoriques**
- **J. C. R. Licklider** : les premiers usages sociaux inattendus de la communication informatique ([[Symbiose homme-machine]]).
- **Marshall McLuhan** : un nouveau média reprend d'abord les conventions du média qu'il remplace ([[Le médium est le message]]).
- **Theodor W. Adorno** : la dimension critique ; la rationalisation industrielle ([[Rationalisation]]) pénètre les relations humaines.
- **Claude Shannon** : la communication comme circulation et compression de l'information ([[Théorie de l'information]]).
- **Pamela Takayoshi et Christina Haas** : les caractéristiques linguistiques de la messagerie instantanée ([[Sociolinguistique]]).
- **Lieke Verheijen** : l'adaptation de la lecture et de l'écriture à une communication rapide et efficace.

**Notions essentielles**

| Notion | Signification dans le chapitre |
|---|---|
| Accélération ([[Accélération sociale\|accélération sociale]]) | Réduction du temps consacré à écrire, lire et répondre |
| Compression ([[Compression de données\|compression de données]]) | Réduction matérielle et linguistique de l'information |
| Asynchronie ([[Communication asynchrone\|communication asynchrone]]) | Possibilité de communiquer sans présence simultanée |
| Optimisation ([[Rationalisation\|rationalisation]]) | Recherche permanente d'une communication plus efficace |
| [[Skeuomorphisme]] | Reprise des formes d'un ancien média dans un nouveau |
| Fragmentation | Multiplication simultanée des conversations et sollicitations |
| Hybridation | Mélange entre texte, oralité, signes et images |
| Attention | Ressource sollicitée par l'augmentation du nombre de messages (voir [[Économie de l'attention]]) |
| [[Nœud (réseau)\|Nœud du réseau]] | L'individu participe lui-même à la circulation et à l'optimisation de l'information |

## Concepts

**Réseaux et Internet** : [[ARPANET]] · [[DARPA]] · [[Interface Message Processor]] · [[BBN]] · [[Commutation de paquets]] · [[Réseau décentralisé]] · [[RAND Corporation]] · [[Protocole de communication]] · [[Suite des protocoles Internet]] · [[Modèle OSI]] · [[Adressage IPv4 et CIDR]] · [[Internet]] · [[Réseau]] · [[Nœud (réseau)]] · [[Routeur]] · [[Satellite de télécommunications]] · [[Modem]] · [[Débit binaire]] · [[Union internationale des télécommunications]] · [[Courrier électronique]] · [[Arobase]] · [[TENEX]] · [[Temps partagé]] · [[Client de messagerie]] · [[Messagerie instantanée]] · [[PLATO (système)]] · [[Unix]]

**Web** : [[World Wide Web]] · [[CERN]] · [[W3C]] · [[URL]] · [[Nom de domaine]] · [[DNS]] · [[HTTP]] · [[Code d'état HTTP]] · [[Chiffrement]] · [[HTML]] · [[Langage de balisage]] · [[Lien hypertexte]] · [[Memex]] · [[Démonstration d'Engelbart]] · [[Modèle client-serveur]] · [[Serveur web]] · [[Navigateur web]] · [[Formulaire web]] · [[Mozilla]] · [[Guerre des navigateurs]] · [[Code source]] · [[Domaine public]] · [[Logiciel libre]] · [[Portail web]] · [[Annuaire web]] · [[Moteur de recherche]] · [[Robot d'indexation]] · [[PageRank]] · [[Google]] · [[Hébergement web]]

**Ordinateur personnel et interfaces** : [[Xerox PARC]] · [[Ordinateur personnel]] · [[Macintosh]] · [[Ordinateur portable]] · [[Dynabook]] · [[Interface graphique]] · [[WIMP]] · [[Souris (informatique)]] · [[Manipulation directe]] · [[Interface en ligne de commande]] · [[Imprimante]] · [[Ethernet]] · [[Réseau local]] · [[IEEE]] · [[Informatique distribuée]] · [[Apple]] · [[Microsoft]] · [[NeXT]] · [[Design d'interaction]] · [[Design d'interface]]

**Silicon Valley et économie** : [[Silicon Valley]] · [[Université Stanford]] · [[SRI International]] · [[Stanford Research Park]] · [[Hewlett-Packard]] · [[Semi-conducteur]] · [[Transistor]] · [[Circuit intégré]] · [[Laboratoires Bell]] · [[Fairchild Semiconductor]] · [[Intel]] · [[Processeur]] · [[Loi de Moore]] · [[Département de la Défense des États-Unis]] · [[Guerre froide]] · [[Spoutnik]] · [[Start-up]] · [[Capital-risque]] · [[Entrepreneuriat]] · [[Introduction en bourse]] · [[Bulle Internet]] · [[Libéralisme économique]] · [[Capitalisme]] · [[Réserve fédérale]] · [[Banque centrale]]

**Idéologies et imaginaires** : [[Idéologie californienne]] · [[Aux sources de l'utopie numérique]] · [[Contre-culture]] · [[Mouvement hippie]] · [[Libertarianisme]] · [[Objectivisme]] · [[La Grève (roman)]] · [[Whole Earth Catalog]] · [[Vente par correspondance]] · [[Geek]] · [[Mondialisation]] · [[Métaphore]] · [[Autoroute de l'information]] · [[Encyclopédie]] · [[Imaginaire]] · [[Cyberespace]] · [[Métavers]] · [[Réalité virtuelle]] · [[Avatar (informatique)]] · [[Transhumanisme]] · [[Cyberpunk]] · [[Science-fiction]] · [[Dystopie]] · [[Le Meilleur des mondes]] · [[1984 (roman)]] · [[Les Portes de la perception]] · [[Le Festin nu]] · [[Tron]] · [[Neuromancer]] · [[Beat Generation]] · [[Psychédélisme]] · [[Seconde Guerre mondiale]] · [[Radar]] · [[Totalitarisme]] · [[Surveillance de masse]] · [[Propagande]] · [[Fabrique du consentement]]

**Cybernétique** : [[Cybernétique]] · [[Conférences Macy]] · [[Information]] · [[Signal (télécommunications)]] · [[Rétroaction]] · [[Homéostasie]] · [[Contrôle (cybernétique)]] · [[Système complexe]] · [[Théorie de l'information]] · [[Bande magnétique]]

**Communication** : [[Communication asynchrone]] · [[Accélération sociale]] · [[SMS]] · [[GSM]] · [[Téléphone mobile]] · [[Langage SMS]] · [[Réseau social]] · [[Le médium est le message]] · [[Correspondance épistolaire]] · [[Poste (service postal)]] · [[Timbre-poste]] · [[Uniform Penny Post]] · [[Alphabétisation]] · [[Skeuomorphisme]] · [[Savoir-vivre]] · [[Norme sociale]] · [[Sociabilité]] · [[Analyse coût-bénéfice]] · [[Impératif de productivité]] · [[Rationalisation]] · [[Raison instrumentale]] · [[Minima Moralia]] · [[École de Francfort]] · [[Génération Y]] · [[Sociolinguistique]] · [[Logogramme]] · [[Compression de données]] · [[Redondance (théorie de l'information)]] · [[Économie de l'attention]] · [[Charge cognitive]] · [[Symbiose homme-machine]] · [[AOL]]
