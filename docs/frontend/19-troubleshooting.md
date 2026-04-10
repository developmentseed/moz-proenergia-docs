---
sidebar_position: 19
title: "Frontend Troubleshooting"
---

# 19. Frontend Troubleshooting

| Issue | Cause & Resolution |
|---|---|
| Map tiles not loading (blank map) | Check network connectivity and refresh. The ScenarioFile's PMTiles may not be generated — contact an administrator to verify file status. |
| Filter panel appears empty | Data Model has no `filter_fields`, or metadata failed to load. Reload the page. Administrator should verify the JSON configuration. |
| Summary statistics not updating | Ensure filters were applied with the **Apply** button. Check browser console (F12) for network errors. |
| Cannot log in | Verify username and password. Contact your Super Admin to reset credentials. |
| Download button is greyed out | Ensure you are logged in. Private datasets require an authenticated session. |
| Popup shows blank or undefined values | The `popup_fields` column name does not match the CSV property name (case-sensitive). Administrator should verify the field name. |
| Scenario dropdown shows only one option | Only scenarios with a ScenarioFile in Ready status are shown. Upload and process Scenario Files via admin. |
| Language toggle not available | The language switcher appears in the header navigation. Reload the page if it is missing. |
| Data in wrong language | Click the PT/EN toggle in the header. If translated content is missing, an administrator must fill in the `name_pt` / `description_pt` fields in the admin. |
| Model not appearing in sidebar | The Data Model's `is_public` flag is `False`. Contact a Super Admin to enable it. |
