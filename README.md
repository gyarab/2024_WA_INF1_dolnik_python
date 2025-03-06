# 2024_WA_INF1_dolnik_python
## Django projekt do předmětu Webových aplikací

### Popis projektu
Tento projekt je sbírka různých her a autorů. V rámci tohoto projektu jsou hry, ke kterým jsou přidělené kategorie a autoři. 

### Funkcionalita
- **Hry**: U každé hry je možné si rozkliknout její detail, kde se zobrazí informace o kategoriích, do kterých hra patří, a o autorovi, který hru vytvořil. Ke hře je vždy přidělen jeden autor ale kategorií může být ke hře přiřazeno více.
- **Autoři**: U každého autora je možné si rozkliknout jeho profil, kde se zobrazí seznam všech her, které tento autor vytvořil. Autor může mít přiřazených více her.
- **Kategorie**: U každé kategorie je možné si rozkliknout její detail, kde se zobrazí seznam všech her, které do této kategorie patří. Kategorii k sobě může mít přiřazeno více her.

### Technologie
Projekt je vytvořen pomocí frameworku Django, který umožňuje snadnou správu databází a vytváření webových aplikací. Pro správu závislostí je použit nástroj pip.

### Použití
Po spuštění serveru můžete přistupovat k aplikaci ve vašem webovém prohlížeči na adrese `http://127.0.0.1:8000/`. Zde můžete procházet hry, autory a kategorie podle výše uvedené funkcionality.