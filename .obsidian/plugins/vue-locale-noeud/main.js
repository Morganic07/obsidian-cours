const { Plugin, TFile } = require("obsidian");

// Clic droit sur un nœud du graphe : Obsidian déclenche « file-menu » avec la
// source « graph-context-menu » et la feuille du graphe en cinquième argument.
module.exports = class VueLocaleNoeud extends Plugin {
  onload() {
    this.registerEvent(
      this.app.workspace.on("file-menu", (menu, file, source, leaf) => {
        if (source !== "graph-context-menu" || !(file instanceof TFile)) return;
        menu.addItem((item) =>
          item
            .setTitle("Ouvrir la vue locale")
            .setIcon("lucide-git-fork")
            .onClick(() => this.ouvrirVueLocale(file, leaf))
        );
      })
    );
  }

  async ouvrirVueLocale(file, leaf) {
    // Même vue que la commande « Ouvrir la vue locale » d'Obsidian, ouverte
    // à droite du graphe pour garder celui-ci visible.
    const cible = leaf
      ? this.app.workspace.createLeafBySplit(leaf, "vertical")
      : this.app.workspace.getLeaf("split");
    await cible.setViewState({
      type: "localgraph",
      active: true,
      state: { file: file.path },
    });
    this.app.workspace.revealLeaf(cible);
  }
};
