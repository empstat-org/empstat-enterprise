// Placeholder sample data for the Enterprise / Establishment Data Coverage Index.
// Illustrative only — replaced automatically on the first pipeline run:
//   cd pipeline && python fetch_and_rank.py --config config_enterprise --out ../web/data
// or a full local sample: python pipeline/gen_enterprise_sample.py
window.RANKINGS = (function () {
  var Y = new Date().getFullYear();
  var IND = [
    { code: "EES_TEES_SEX_AGE_NB",     label: "Employees",                             tier: 1, weight: 2.0 },
    { code: "EMP_TEMP_SEX_ECO_NB",     label: "Employment by economic activity",       tier: 1, weight: 2.0 },
    { code: "EAR_EMTA_SEX_ECO_CUR_NB", label: "Average monthly earnings of employees",  tier: 1, weight: 1.5 },
    { code: "EAR_EHRA_SEX_ECO_CUR_NB", label: "Average hourly earnings of employees",   tier: 1, weight: 1.5 },
    { code: "HOW_TEMP_SEX_ECO_NB",     label: "Mean weekly hours actually worked",      tier: 1, weight: 1.5 },
    { code: "EES_TEES_SEX_AGE_ECO_NB", label: "Employees by economic activity",         tier: 2, weight: 1.0 },
    { code: "EES_TEES_SEX_AGE_INS_NB", label: "Employees by public / private sector",   tier: 2, weight: 1.0 },
    { code: "LAC_XEES_ECO_CUR_NB",     label: "Average hourly labour cost per employee", tier: 2, weight: 1.0 },
    { code: "EMP_TEMP_SEX_STE_NB",     label: "Employment by status in employment",     tier: 2, weight: 1.0 }
  ];
  var THRESH = [0.30, 0.35, 0.45, 0.55, 0.45, 0.55, 0.60, 0.70, 0.50];
  function clamp(x) { return Math.max(0, Math.min(100, x)); }
  function mk(iso, country, region, mat) {
    var lag = mat >= 0.85 ? 1 : mat >= 0.65 ? 2 : mat >= 0.45 ? 4 : 7;
    var per = mat >= 0.85 ? "Q" : "A";
    var latest = Y - lag, sumW = 0, gotW = 0, nCov = 0, inds = {};
    IND.forEach(function (i, idx) {
      var cov = mat >= THRESH[idx];
      sumW += i.weight;
      if (cov) { gotW += i.weight; nCov++; }
      inds[i.code] = { covered: cov, latest: cov ? latest : null, periodicity: cov ? per : null };
    });
    var coverage = Math.round(1000 * gotW / sumW) / 10;
    var pts = { M: 100, Q: 85, A: 60 }[per];
    var frequency = Math.round((pts + mat * 100) / 2 * 10) / 10;
    var recency = Math.round(clamp(100 * (12 - lag) / 11) * 10) / 10;
    var src = mat >= 0.7
      ? [{ name: "Establishment survey", latest: latest }, { name: "Social security records", latest: latest }]
      : [{ name: "Establishment survey", latest: latest }];
    return {
      iso3: iso, country: country, region: region,
      coverage: coverage, frequency: frequency, recency: recency,
      latest_year: latest, best_periodicity: per,
      n_covered: nCov, n_total: IND.length, sources: src, indicators: inds
    };
  }
  var ROWS = [
    ["DEU", "Germany", "Europe and Central Asia", 0.96],
    ["FRA", "France", "Europe and Central Asia", 0.95],
    ["GBR", "United Kingdom", "Europe and Central Asia", 0.94],
    ["USA", "United States", "Americas", 0.95],
    ["CAN", "Canada", "Americas", 0.92],
    ["JPN", "Japan", "Asia and the Pacific", 0.91],
    ["KOR", "Korea, Republic of", "Asia and the Pacific", 0.90],
    ["AUS", "Australia", "Asia and the Pacific", 0.90],
    ["BRA", "Brazil", "Americas", 0.80],
    ["ZAF", "South Africa", "Africa", 0.78],
    ["MEX", "Mexico", "Americas", 0.76],
    ["TUR", "Türkiye", "Europe and Central Asia", 0.74],
    ["MYS", "Malaysia", "Asia and the Pacific", 0.66],
    ["MAR", "Morocco", "Africa", 0.58],
    ["KEN", "Kenya", "Africa", 0.50],
    ["JOR", "Jordan", "Arab States", 0.52],
    ["PHL", "Philippines", "Asia and the Pacific", 0.62],
    ["IND", "India", "Asia and the Pacific", 0.55],
    ["NGA", "Nigeria", "Africa", 0.40],
    ["SAU", "Saudi Arabia", "Arab States", 0.60]
  ];
  return {
    generated: "placeholder",
    current_year: Y,
    index_name: "Enterprise / Establishment Data Coverage Index",
    source: "PLACEHOLDER SAMPLE — replace via fetch_and_rank.py --config config_enterprise",
    is_sample: true,
    default_weights: { coverage: 1.0, frequency: 1.0, recency: 1.0 },
    scoring_params: {
      coverage: { coverage_window_years: 15 },
      frequency: { periodicity_points: { M: 100, Q: 85, A: 60, irregular: 30 }, regularity_window_years: 10 },
      recency: { full_marks_max_age: 1, zero_marks_min_age: 12 }
    },
    indicators: IND,
    countries: ROWS.map(function (r) { return mk(r[0], r[1], r[2], r[3]); })
  };
})();
