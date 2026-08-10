# Enterprise / Establishment Data Coverage Index

One of the Empstat labour-data coverage indices. This repo is self-contained and
deploys to **https://enterprise.empstat.org** via GitHub Pages.

Ranks countries by how well their **company-level** labour statistics are covered
in ILOSTAT — the series collected from establishments / enterprises rather than
households: employees, employment and earnings by economic activity, hours of
work, labour cost, and related. It counts **all business-level sources**
(establishment & enterprise surveys, economic / establishment censuses, and
register / social-security records) and excludes household / labour-force surveys,
population censuses, and modelled or official estimates.

- Site: `web/index.html` (reads `web/data/rankings.js`)
- Custom domain: `web/CNAME` = enterprise.empstat.org
- Config: `pipeline/config_enterprise.py` (indicator set, source filter, scoring)
- Pipeline: refresh real data with:
  ```
  cd pipeline
  pip install -r requirements.txt
  python fetch_and_rank.py --config config_enterprise --out ../web/data
  ```
- Illustrative sample data (no network needed): `python pipeline/gen_enterprise_sample.py`
- Weekly auto-refresh + deploy: `.github/workflows/weekly-update.yml` (Mondays 22:00 UTC, and on every push)

Sibling sites: lfs.empstat.org · census.empstat.org · admin.empstat.org · enterprise.empstat.org.
Data: ILOSTAT (CC BY 4.0). Independent index; not published or endorsed by the ILO.
