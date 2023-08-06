import adsctl as ads

google_ads = ads.GoogleAds()

query = """
SELECT
    metrics.impressions,
    metrics.clicks,
    metrics.cost_micros
FROM user_location_view
WHERE segments.date BETWEEN '20230601' AND '20230630'
"""


summary = google_ads.create_client().enums.SummaryRowSettingEnum.SUMMARY_ROW_ONLY

results = google_ads.query(query, summary_row_setting=summary)

for table, df in results.items():
    print(table)
    print(df)
