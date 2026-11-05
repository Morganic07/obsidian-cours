## 7. Différences entre Pointeur et Double Pointeur

| POINTEUR | DOUBLE POINTEUR |
|---|---|
| Contient l'adresse d'une variable. | Contient l'adresse d'un pointeur. |
| Utilisé pour manipuler directement des variables. | Utilisé pour manipuler des pointeurs. |
| Accès via un astérisque (`*`). | Accès via deux astérisques (`**`). |

---

## 8. Précautions avec les Doubles Pointeurs

1. **Initialisation obligatoire :** Assurez-vous que les pointeurs (et doubles pointeurs) sont correctement initialisés avant utilisation.
2. **Gestion de mémoire :** Pour chaque `malloc` sur un pointeur, assurez-vous d'appeler `free`.
3. **Vérification des pointeurs NULL :** Avant d'accéder à un double pointeur, vérifiez que les pointeurs sont non nuls.
