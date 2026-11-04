-- Filtre pandoc : rend les tableaux des Docs utilisables dans Obsidian.
-- Sans lui, pandoc les écrit en HTML brut, où les liens [[...]] ne fonctionnent pas.

local SAUT = pandoc.RawInline("html", "<br>")

-- Sans attributs de taille, pandoc écrit ![](...) au lieu d'une balise <img>.
function Image(img)
  return pandoc.Image(img.caption, img.src)
end

local function lignes(t)
  local toutes = pandoc.List()
  toutes:extend(t.head.rows)
  for _, corps in ipairs(t.bodies) do
    toutes:extend(corps.head)
    toutes:extend(corps.body)
  end
  toutes:extend(t.foot.rows)
  return toutes
end

-- Ramène des blocs à une suite de lignes d'une seule cellule.
-- Renvoie nil si un bloc ne peut pas tenir dans une cellule (code, tableau imbriqué).
local function aplatir(blocs)
  local morceaux = pandoc.List()
  for _, bloc in ipairs(blocs) do
    if bloc.t == "Para" or bloc.t == "Plain" then
      morceaux:insert(bloc.content)
    elseif bloc.t == "Header" then
      morceaux:insert(pandoc.Inlines({ pandoc.Strong(bloc.content) }))
    elseif bloc.t == "BulletList" or bloc.t == "OrderedList" then
      for _, element in ipairs(bloc.content) do
        local dedans = aplatir(element)
        if not dedans then return nil end
        for _, ligne in ipairs(dedans) do
          local puce = pandoc.Inlines({ pandoc.Str("•"), pandoc.Space() })
          puce:extend(ligne)
          morceaux:insert(puce)
        end
      end
    elseif bloc.t == "BlockQuote" or bloc.t == "Div" then
      local dedans = aplatir(bloc.content)
      if not dedans then return nil end
      morceaux:extend(dedans)
    elseif bloc.t ~= "RawBlock" then
      return nil
    end
  end
  return morceaux
end

function Table(t)
  if #t.colspecs == 1 then
    local blocs = pandoc.List()
    for _, ligne in ipairs(lignes(t)) do
      for _, cellule in ipairs(ligne.cells) do
        blocs:extend(cellule.contents)
      end
    end
    if #blocs == 0 then return {} end
    blocs:insert(1, pandoc.RawBlock("markdown", "[!note]"))
    return pandoc.BlockQuote(blocs)
  end

  for _, ligne in ipairs(lignes(t)) do
    for _, cellule in ipairs(ligne.cells) do
      local morceaux = aplatir(cellule.contents)
      if morceaux then
        local suite = pandoc.Inlines({})
        for i, m in ipairs(morceaux) do
          if i > 1 then suite:insert(SAUT) end
          suite:extend(m)
        end
        cellule.contents = pandoc.Blocks({ pandoc.Plain(suite) })
      end
    end
  end
  return t
end
