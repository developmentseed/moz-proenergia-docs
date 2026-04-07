#!/usr/bin/env python3
"""
generate_docs.py — generates a complete Docusaurus v3 site for the
IEP PROENERGIA+ Platform User Guide.

Usage:
    python generate_docs.py [output_dir]

Output defaults to ./proenergia-docs
"""

import os, sys, textwrap

OUT = sys.argv[1] if len(sys.argv) > 1 else "proenergia-docs"

FILES = {}   # path → content


# ─── helpers ──────────────────────────────────────────────────────────────
def f(path, content):
    FILES[path] = textwrap.dedent(content).lstrip("\n")

def write_all():
    for path, content in FILES.items():
        full = os.path.join(OUT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(content)
    print(f"✓ wrote {len(FILES)} files to {OUT}/")


# ══════════════════════════════════════════════════════════════════════════
# DOCUSAURUS CONFIG FILES
# ══════════════════════════════════════════════════════════════════════════

f("docusaurus.config.js", """
    // @ts-check
    const {themes} = require('prism-react-renderer');

    /** @type {import('@docusaurus/types').Config} */
    const config = {
      title: 'IEP PROENERGIA+',
      tagline: 'Platform User Guide — MIREME UIPCE · SE4ALL · Development Seed',
      favicon: 'img/favicon.ico',
      url: 'https://your-domain.com',
      baseUrl: '/',
      onBrokenLinks: 'throw',
      onBrokenMarkdownLinks: 'warn',
      i18n: { defaultLocale: 'en', locales: ['en'] },

      presets: [
        ['classic', /** @type {import('@docusaurus/preset-classic').Options} */ ({
          docs: {
            sidebarPath: require.resolve('./sidebars.js'),
            routeBasePath: '/',
          },
          blog: false,
          theme: { customCss: require.resolve('./src/css/custom.css') },
        })],
      ],

      themeConfig: /** @type {import('@docusaurus/preset-classic').ThemeConfig} */ ({
        navbar: {
          title: 'IEP PROENERGIA+',
          items: [
            { type: 'docSidebar', sidebarId: 'docs', position: 'left', label: 'Documentation' },
          ],
        },
        prism: {
          theme: themes.github,
          darkTheme: themes.dracula,
          additionalLanguages: ['bash', 'json', 'python', 'nginx'],
        },
      }),
    };

    module.exports = config;
""")

f("sidebars.js", """
    /** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
    const sidebars = {
      docs: [
        { type: 'doc', id: 'intro', label: 'Introduction' },
        {
          type: 'category',
          label: 'Backend',
          collapsed: false,
          items: [
            'backend/02-accessing-admin',
            'backend/03-user-management',
            'backend/04-data-models',
            'backend/05-json-configuration',
            'backend/06-scenarios',
            'backend/07-vector-datasets',
            'backend/08-raster-datasets',
            'backend/09-reference-datasets',
            'backend/10-monitoring',
            'backend/11-api-reference',
          ],
        },
        {
          type: 'category',
          label: 'Frontend',
          collapsed: false,
          items: [
            'frontend/12-interface-overview',
            'frontend/13-model-navigation',
            'frontend/14-filter-panel',
            'frontend/15-map-panel',
            'frontend/16-summary-panel',
            'frontend/17-downloads',
            'frontend/18-content-pages',
            'frontend/19-troubleshooting',
          ],
        },
        {
          type: 'category',
          label: 'Deployment',
          items: [
            'deployment/20-server-requirements',
            'deployment/21-deployment-overview',
            'deployment/22-environment-configuration',
            'deployment/23-post-installation',
            'deployment/24-update-procedures',
            'deployment/25-backup-recovery',
            'deployment/26-troubleshooting',
          ],
        },
        {
          type: 'category',
          label: 'Appendices',
          items: [
            'appendices/a-json-skeletons',
            'appendices/b-admin-columns',
            'appendices/c-permissions',
            'appendices/d-glossary',
          ],
        },
      ],
    };

    module.exports = sidebars;
""")

f("src/css/custom.css", """
    :root {
      --ifm-color-primary: #1a4f8a;
      --ifm-color-primary-dark: #164475;
      --ifm-color-primary-darker: #143e6d;
      --ifm-color-primary-darkest: #10325a;
      --ifm-color-primary-light: #1e5a9f;
      --ifm-color-primary-lighter: #2060a7;
      --ifm-color-primary-lightest: #2b6fba;
      --ifm-code-font-size: 90%;
    }
    .docusaurus-highlight-code-line {
      background-color: rgba(0, 0, 0, 0.1);
      display: block;
      margin: 0 calc(-1 * var(--ifm-pre-padding));
      padding: 0 var(--ifm-pre-padding);
    }
""")

f("package.json", """
    {
      "name": "proenergia-docs",
      "version": "1.0.0",
      "private": true,
      "scripts": {
        "docusaurus": "docusaurus",
        "start": "docusaurus start",
        "build": "docusaurus build",
        "serve": "docusaurus serve"
      },
      "dependencies": {
        "@docusaurus/core": "^3.5.0",
        "@docusaurus/preset-classic": "^3.5.0",
        "clsx": "^2.0.0",
        "prism-react-renderer": "^2.3.0",
        "react": "^18.0.0",
        "react-dom": "^18.0.0"
      }
    }
""")

f(".gitignore", """
    node_modules/
    .docusaurus/
    build/
""")


# ══════════════════════════════════════════════════════════════════════════
# INTRO
# ══════════════════════════════════════════════════════════════════════════

f("docs/intro.md", """
    ---
    id: intro
    sidebar_position: 1
    title: Introduction
    ---

    # IEP PROENERGIA+ Platform User Guide

    **MIREME UIPCE · SE4ALL · Development Seed** — Version 1.2 · 2026

    PROENERGIA+ IEP is a spatial data infrastructure and visualization platform for integrated electrification planning in Mozambique. It enables national and provincial decision-makers to explore energy access scenarios using the latest geospatial data, analyze settlement-level outcomes, and export actionable insights.

    This guide is divided into three parts:

    - **[Backend](./backend/02-accessing-admin)** — Django Admin interface, user management, data model configuration, scenario and dataset management, JSON configuration, and API reference.
    - **[Frontend](./frontend/12-interface-overview)** — Visualization interface, filter controls, map interaction, scenario selection, analysis summaries, and downloads.
    - **[Deployment](./deployment/20-server-requirements)** — Server setup, systemd services, Nginx, Celery, RabbitMQ, environment variables, and update procedures.

    ## System Architecture

    | Component | Description |
    |-----------|-------------|
    | Backend API (Django REST) | Serves data to the frontend. Django + DRF, backed by PostgreSQL 16 / PostGIS. Admin at `/admin/`. API at `/api/v1/`. |
    | Task Queue (Celery / RabbitMQ) | Background workers for file conversion (GDAL → FlatGeobuf → PMTiles via Tippecanoe). |
    | Frontend (Next.js / TypeScript) | MapLibre GL mapping + Chakra UI. Supports English and Portuguese (default). |
    | Object Storage | Stores uploaded source files and derived PMTiles. |
    | Tile Delivery (PMTiles) | Vector tiles via HTTP range requests. Raster layers via Cloud-Optimized GeoTIFF (COG). |
""")


# ══════════════════════════════════════════════════════════════════════════
# BACKEND
# ══════════════════════════════════════════════════════════════════════════

f("docs/backend/02-accessing-admin.md", """
    ---
    sidebar_position: 2
    title: "2. Accessing the Admin Interface"
    ---

    # 2. Accessing the Django Admin Interface

    ## 2.1 URL and Login

    The Django Admin is accessible at:

    - **Production:** `https://<your-deployment-domain>/admin/`
    - **Local development:** `http://localhost:8000/admin/`

    Log in with a staff or superuser account. Navigate to the login page, enter your credentials, and click **Log In**.

    :::note
    On a fresh deployment, a superuser must be created via the command line before anyone can log in. See Section 2.3.
    :::

    ## 2.2 Admin Home Screen

    After logging in, the admin home lists all registered model groups:

    - **Authentication and Authorization** — User and Group management
    - **Datasets** — DataModel, VectorDataset, VectorFile, RasterDataset, RasterFile, ReferenceDataset, ReferenceFile, Scenario, ScenarioFile

    ## 2.3 Creating the Initial Superuser (CLI)

    ```bash
    cd /var/www/proenergia/app
    source venv/bin/activate
    python manage.py createsuperuser
    ```

    :::note
    Superuser accounts should be restricted to a small number of trusted administrators. Use staff-level Admin accounts for day-to-day management.
    :::
""")

f("docs/backend/03-user-management.md", """
    ---
    sidebar_position: 3
    title: "3. User Management"
    ---

    # 3. User Management

    ## 3.1 User Roles and Permissions

    | Permission | User | Admin | Super Admin |
    |------------|:----:|:-----:|:-----------:|
    | **VIEW ALL DATA** | | | |
    | View & explore public Data Models (frontend) | ✓ | ✓ | ✓ |
    | View private Data Models (frontend / API) | — | — | ✓ |
    | Download public datasets | ✓ | ✓ | ✓ |
    | Download private datasets | — | ✓ | ✓ |
    | **DATA MANAGEMENT** | | | |
    | Upload vector / raster / reference files | — | ✓ | ✓ |
    | Edit dataset metadata and JSON configuration | — | ✓ | ✓ |
    | Delete datasets | — | — | ✓ |
    | Add / edit Data Models | — | ✓ | ✓ |
    | Set Data Model `is_public` flag | — | — | ✓ |
    | Add / edit Scenarios and Scenario Files | — | ✓ | ✓ |
    | Publish / unpublish datasets (`is_approved`) | — | — | ✓ |
    | **USER MANAGEMENT** | | | |
    | Create / edit / delete user accounts | — | — | ✓ |

    ### How roles map to Django flags

    | Django flags | Role |
    |---|---|
    | `is_staff = False`, `is_superuser = False` | Standard User — frontend only, no admin access. |
    | `is_staff = True`, `is_superuser = False` | Admin — can access admin, manage their own datasets and scenarios. Cannot manage users or publish datasets. |
    | `is_staff = True`, `is_superuser = True` | Super Admin — bypasses all permission checks. Full access to everything. |

    ## 3.2 Creating a New User

    1. Go to **Authentication and Authorization → Users → + Add User**.
    2. Enter a username and password, then click **Save and continue editing**.
    3. Fill in personal information (first name, last name, email).
    4. Set the appropriate permission level (see Section 3.3). Click **Save**.

    ## 3.3 Setting a User's Role

    | Checkbox | Effect |
    |---|---|
    | **Active** (checked) | Account is active. Uncheck to disable without deleting. |
    | **Staff status** (checked) | Grants access to the Django Admin. Required for Admin and Super Admin roles. |
    | **Superuser status** (checked) | Full unrestricted access. Required for Super Admin role. |

    - **Standard User:** Leave both unchecked.
    - **Admin:** Check Staff status only. Optionally assign specific model-level permissions.
    - **Super Admin:** Check both Staff status and Superuser status.

    ## 3.4 Assigning Specific Permissions to Admin Users

    In the **User Permissions** multi-select, grant:

    - `datasets | data model | Can add/change/view data model`
    - `datasets | vector dataset | Can add/change/view vector dataset`
    - `datasets | vector file | Can add/change/view vector file`
    - `datasets | raster dataset | Can add/change/view raster dataset`
    - `datasets | reference dataset | Can add/change/view reference dataset`
    - `datasets | scenario | Can add/change/view scenario`
    - `datasets | scenario file | Can add/change/view scenario file`

    :::note
    Super Admin accounts bypass all granular permission checks. Specific permissions only need to be set for staff-level Admin accounts.
    :::

    ## 3.5 Editing and Deactivating Users

    Go to **Authentication and Authorization → Users** and click a username to edit. To deactivate without deleting, uncheck the **Active** checkbox and click **Save**.
""")

f("docs/backend/04-data-models.md", """
    ---
    sidebar_position: 4
    title: "4. Data Models"
    ---

    # 4. Data Models

    ## 4.1 What Is a Data Model?

    A Data Model represents a planning or analysis category — such as Least Cost Electrification, Agricultural Cold Chain, or Clean Cooking. Each Data Model groups together Scenarios, Vector Datasets, and display configuration (filters, popups, summaries, colour coding). It can also reference Raster layers (COG imagery) and Reference datasets (documents).

    ## 4.2 Adding a New Data Model

    1. Go to **Datasets → Data Models → + Add Data Model**.
    2. Fill in the top-level fields (see Section 4.3).
    3. Add JSON configuration for `filter_fields`, `popup_fields`, `summary_fields`, and `color_coding` (see [Section 5](./05-json-configuration)).
    4. Click **Save**, or **Save and continue editing**.

    ## 4.3 Data Model Fields Reference

    | Field | Description |
    |---|---|
    | **Name / Name (PT)** | Unique name (max 155 chars). Supports English and Portuguese via the tabbed form. Displayed in the frontend navigation sidebar. |
    | **Description / Description (PT)** | Optional description. Supports translations. |
    | **Presentation Order** | Integer controlling sort order in the frontend sidebar. Lower numbers appear first. Default: 0. |
    | **Is Public** | Boolean (default: True). If False, the model is hidden from the API for non-superusers and does not appear on the frontend. |
    | **Visualization Column** | Optional. The exact CSV column name whose unique values colour-code map features. Leave blank for a single default colour. |
    | **Color Coding (JSON)** | Maps each visualization column value to a hex colour. See [Section 5.4](./05-json-configuration#54-color_coding). |
    | **Filter Fields (JSON)** | Controls filter controls in the left panel. See [Section 5.1](./05-json-configuration#51-filter_fields). |
    | **Popup Fields (JSON)** | Defines attributes shown when a user clicks a map feature. See [Section 5.2](./05-json-configuration#52-popup_fields). |
    | **Summary Fields (JSON)** | Specifies aggregated statistics in the right-panel summary. See [Section 5.3](./05-json-configuration#53-summary_fields). |
    | **Contextual Layers** | Multi-select of approved VectorDatasets to toggle on/off alongside the main data. |
    | **Raster Layers** | Multi-select of approved RasterDatasets (COG imagery). |
    | **Reference Datasets** | Multi-select of approved ReferenceDatasets (documents, tables). |

    :::warning
    Changes to JSON configuration fields affect all users immediately. Test carefully before saving in production.
    :::

    :::tip JSON editor
    The JSON fields use an interactive tree/form/view/code editor. Switch between modes using the tabs above each field. **Code** mode accepts raw JSON text.
    :::
""")

f("docs/backend/05-json-configuration.md", """
    ---
    sidebar_position: 5
    title: "5. JSON Configuration Fields"
    ---

    # 5. JSON Configuration Fields

    Four JSON arrays on each Data Model configure frontend behaviour. The admin validates structure on save and reports errors for missing required keys or invalid values.

    :::note
    All JSON must use double quotes for keys and string values, with no trailing commas. Arrays must be wrapped in `[ ]`.
    :::

    ---

    ## 5.1 `filter_fields`

    Defines the filter controls shown in the left panel. Each entry maps to one interactive filter control.

    ### Schema

    | Key | Type | Required? | Description |
    |---|---|---|---|
    | `label` | string | **required** | Human-readable label shown above the filter control. |
    | `description` | string | **required** | Tooltip text. Can be an empty string. |
    | `column` | string | **required** | Exact column name in the scenario CSV. **Case-sensitive.** |
    | `label_pt` | string | optional | Portuguese translation of the label. |
    | `description_pt` | string | optional | Portuguese translation of the description. |

    ### How filter type is determined

    The frontend derives the control type at runtime from the column name and data values:

    | Derived Type | Condition | Rendered Control |
    |---|---|---|
    | `admin` | Column name matches an administrative geography keyword (Admin_1–4, Province, Província, District, Distrito, Posto, Localidade, Region, Região, and plural/accented variants) | Searchable multi-select Combobox |
    | `numeric` | Column data contains numeric values (not all 0 or 1) | Dual text-input range control |
    | `checkbox` | All other cases (strings, booleans) | Checkbox group |

    ### Example

    ```json
    [
      {
        "label": "Province",
        "description": "Administrative province",
        "label_pt": "Provincia",
        "description_pt": "Provincia administrativa",
        "column": "Admin_1"
      },
      {
        "label": "Electrification Technology",
        "description": "Recommended technology for 2030",
        "column": "Technology2030"
      },
      {
        "label": "Population (2030)",
        "description": "Projected settlement population",
        "column": "Pop2030"
      }
    ]
    ```

    :::tip
    `Admin_1` → admin combobox. `Technology2030` → checkbox group (string values). `Pop2030` → numeric range control.
    :::

    ---

    ## 5.2 `popup_fields`

    Defines which attributes are displayed when a user clicks a feature on the map. Fields appear in the order listed.

    ### Schema

    | Key | Type | Required? | Description |
    |---|---|---|---|
    | `label` | string | **required** | Display label for the attribute. |
    | `description` | string | **required** | Tooltip text. Can be an empty string. |
    | `column` | string | **required** | Exact CSV column name. **Case-sensitive.** |
    | `label_pt` | string | optional | Portuguese translation of the label. |
    | `description_pt` | string | optional | Portuguese translation of the description. |

    :::note
    When a user clicks a feature, the frontend calls `GET /api/v1/scenario/{id}/feature/{feature_id}/` and shows only the columns listed here, in order.
    :::

    ### Example

    ```json
    [
      {
        "label": "Settlement Name",
        "description": "Name of the settlement",
        "label_pt": "Nome do Assentamento",
        "description_pt": "Nome do assentamento",
        "column": "SettlementName"
      },
      { "label": "Population (2030)", "description": "Projected population", "column": "Pop2030" },
      { "label": "Recommended Technology", "description": "Least-cost technology", "column": "Technology2030" },
      { "label": "Total Investment", "description": "Total investment (USD)", "column": "InvestmentCostTotal" }
    ]
    ```

    ---

    ## 5.3 `summary_fields`

    Defines the aggregated statistics shown in the right-hand Summary panel.

    ### Schema

    | Key | Type | Required? | Description |
    |---|---|---|---|
    | `label` | string | **required** | Display heading for this summary item. |
    | `description` | string | **required** | Tooltip description. Can be empty string. |
    | `columns` | array of strings | **required** | One or more CSV column names. **Always an array.** Multiple columns become sub-rows. |
    | `method` | string | optional | `sum` \\| `average` \\| `count` \\| `min` \\| `max`. Defaults to `sum`. |
    | `unit` | string | optional | Unit suffix after the value, e.g. `"USD"`, `"kW"`, `"km"`. |
    | `group_by` | string or array | optional | Column name(s) to group results by. Single string or array of up to 2 strings for nested grouping. |
    | `category` | string | optional | Groups items under a collapsible heading in the summary panel. |
    | `chartType` | string | optional | `bar` \\| `donut` \\| `stacked` \\| `column` \\| `area` \\| `highlight`. Admin validates all six values. |
    | `colors` | object | optional | Colour map for charts. Keys are data values; values are hex strings. E.g. `{"SHS": "#F1C40F"}`. |
    | `hasDecimal` | boolean | optional | If `true`, values display with decimal places. Must be exactly `true` or `false`. |
    | `showChartValueRows` | boolean | optional | If `true`, shows a table of raw values beneath the chart. |
    | `showBarChartAverage` | boolean | optional | If `true`, overlays an average line on bar charts. |
    | `label_pt` | string | optional | Portuguese translation of the label. |
    | `description_pt` | string | optional | Portuguese translation of the description. |

    :::note
    If `method` is omitted the system defaults to `sum`. For string-type columns, the frontend always uses `count` regardless of the method setting.
    :::

    ### Examples

    **Simple numeric aggregate:**
    ```json
    {
      "label": "Total Population (2030)",
      "description": "Sum of projected population across all settlements",
      "columns": ["Pop2030"],
      "method": "sum"
    }
    ```

    **Technology breakdown as a bar chart with colours:**
    ```json
    {
      "label": "Technology Mix (2030)",
      "description": "Count per electrification technology",
      "columns": ["Technology2030"],
      "method": "count",
      "chartType": "bar",
      "colors": { "SHS": "#F1C40F", "MiniGrid": "#27AE60", "Grid": "#2980B9" },
      "showChartValueRows": true
    }
    ```

    **Numeric field grouped by technology:**
    ```json
    {
      "label": "Investment by Technology",
      "description": "Total investment grouped by technology type",
      "columns": ["InvestmentCostTotal"],
      "method": "sum",
      "unit": "USD",
      "group_by": "Technology2030",
      "chartType": "bar",
      "showBarChartAverage": true
    }
    ```

    **Multi-column aggregate:**
    ```json
    {
      "label": "Capacity by Type",
      "description": "New capacity installed by technology category",
      "columns": ["NewCapacityGrid", "NewCapacityMiniGrid", "NewCapacitySHS"],
      "method": "sum",
      "unit": "kW"
    }
    ```

    ---

    ## 5.4 `color_coding`

    Maps values of `visualization_column` to specific colours on the map. The special value `"default"` sets the fallback colour. The admin validates that each `color` is a valid hex string (3 or 6 hex digits, with or without leading `#`).

    ### Schema

    | Key | Type | Required? | Description |
    |---|---|---|---|
    | `value` | string | **required** | The column value to match. Use `"default"` as a catch-all fallback. |
    | `color` | string | **required** | Valid hex colour string. E.g. `"#E74C3C"` or `"E74C3C"`. Validated by the admin. |

    ### Example

    ```json
    [
      { "value": "SHS",      "color": "#F1C40F" },
      { "value": "MiniGrid", "color": "#27AE60" },
      { "value": "Grid",     "color": "#2980B9" },
      { "value": "default",  "color": "#95A5A6" }
    ]
    ```

    :::warning
    The admin validates hex codes. An invalid value like `"red"` or `"#GG0000"` will produce an error on save.
    :::
""")

f("docs/backend/06-scenarios.md", """
    ---
    sidebar_position: 6
    title: "6. Scenarios & Scenario Files"
    ---

    # 6. Scenarios and Scenario Files

    ## 6.1 What Is a Scenario?

    A Scenario represents a specific model run within a Data Model — for example, *Baseline 2025* or *Accelerated Grid Expansion 2035*. Each Scenario links to a Vector Dataset for spatial geometry and holds analysis results via one or more Scenario Files (CSV).

    ## 6.2 Adding a New Scenario

    1. Go to **Datasets → Scenarios → + Add Scenario**.
    2. Fill in the fields (see Section 6.3).
    3. Click **Save**. You can then add Scenario Files.

    ## 6.3 Scenario Fields Reference

    | Field | Description |
    |---|---|
    | **Name / Name (PT)** | Unique name (max 155 chars). Displayed in the frontend scenario dropdown. Supports EN/PT translations. |
    | **Model** | The Data Model this scenario belongs to (foreign key). |
    | **Vector Dataset** | The Vector Dataset providing spatial geometry for this scenario's map layer. Must have at least one file in Ready status. |
    | **Presentation Order** | Integer controlling sort order in the frontend dropdown. Lower numbers appear first. |

    :::note
    A single Vector Dataset can be shared across multiple Scenarios. Scenarios are ordered in the dropdown by Presentation Order, then by ID.
    :::

    ## 6.4 Adding Scenario Files

    A Scenario File is a CSV containing analysis result data. Each row corresponds to a spatial feature identified by a numeric `id` column. Uploading triggers a Celery task that merges the CSV with vector geometry to generate a PMTiles map layer, then imports the CSV into the database for summary queries.

    1. Go to **Datasets → Scenario Files → + Add Scenario File**.
    2. Select the parent Scenario.
    3. Upload a CSV file. The CSV **must include an `id` column** matching feature IDs in the linked Vector Dataset.
    4. Optionally tick **Represent features as points in lower zoom levels** (see Section 6.5).
    5. Click **Save**.

    :::note CSV format
    Delimiter is auto-detected (comma or semicolon). Numeric strings are automatically converted to numbers; all other values are stored as strings. The `id` column is used as the join key and is not stored as metadata. Files with UTF-8 BOM are handled correctly.
    :::

    ## 6.5 Low Zoom as Points Option

    The **Represent features as points in lower zoom levels** checkbox (`low_zoom_as_points`) optimises rendering for large polygon datasets.

    When enabled, the pipeline generates:
    - Centroid points for zoom levels 5–10
    - Full polygon geometry for zoom levels 11–14
    - These are joined into a single PMTiles file using Tippecanoe's `tile-join` tool.

    :::tip
    Recommended for large datasets (10,000+ features) composed of uniform square polygons. Not necessary for point or line data.
    :::

    ## 6.6 Scenario File Status Indicator

    The Scenario Files list includes an **Is Active** column indicating whether a file is the currently active (latest Ready) file for its scenario. Only the most recently processed Ready file is active.

    ## 6.7 Monitoring Scenario File Processing

    Status progresses: `Created → Processing → Ready` (or `Error`).

    If a file enters Error state, open the record and read the **Error Message** field. Use the **Reprocess files** action to re-queue files in Ready or Error state.

    :::note Cache
    Summary responses are cached for 24 hours. After uploading new data, use `DELETE /api/v1/scenario/{id}/summaries/cache/` to clear stale cached results.
    :::
""")

f("docs/backend/07-vector-datasets.md", """
    ---
    sidebar_position: 7
    title: "7. Vector Datasets & Vector Files"
    ---

    # 7. Vector Datasets and Vector Files

    ## 7.1 What Is a Vector Dataset?

    A Vector Dataset is a named container for spatial geometry — the collection of points, lines, or polygons rendered on the map. Scenarios reference a Vector Dataset to obtain their spatial geometry.

    ## 7.2 Adding a New Vector Dataset

    1. Go to **Datasets → Vector Datasets → + Add Vector Dataset**.
    2. Fill in the metadata fields (see Section 7.3).
    3. Click **Save**. You can then upload Vector Files.

    ## 7.3 Vector Dataset Fields Reference

    | Field | Description |
    |---|---|
    | **Name / Name (PT)** | Unique name (max 155 chars). Supports EN/PT translations. |
    | **Description / Description (PT)** | Optional abstract. Supports translations. |
    | **Data Owner** (`source`) | Optional attribution (max 155 chars). |
    | **Point of Contact** (`contact`) | Optional contact person or team. |
    | **Publication Date** (`published`) | Optional date the dataset was published at the source. |
    | **Temporal Extent** | Optional time period the data covers (e.g. `"2020–2024"`). |
    | **CRS** | Optional. Document the source CRS (e.g. `"EPSG:4326"`). All files are reprojected to EPSG:4326 during processing. |
    | **Maintenance Frequency** | Optional. How often the dataset is updated at the source. |
    | **Lineage** | Optional. Data provenance or processing notes. |
    | **Legal License** | Optional. Licence under which the data is provided. |
    | **Attribute Definitions** | Optional. Link or note describing the attribute schema. |
    | **Is Public** | Superuser only. If ticked, dataset visible to unauthenticated users. |
    | **Is Approved** | Superuser only. Must be approved before the dataset can be used in Scenarios or shown on the frontend. |

    ## 7.4 Adding Vector Files

    Uploading triggers a Celery task: file → FlatGeobuf (GDAL) → PMTiles (Tippecanoe).

    1. Go to **Datasets → Vector Files → + Add Vector File**.
    2. Select the parent Vector Dataset.
    3. Upload a file. Accepted formats:

    | Format | Notes |
    |---|---|
    | `.geojson` | GeoJSON. Must use WGS84 (EPSG:4326). Preferred format. |
    | `.gpkg` | GeoPackage. Fully supported. |
    | `.zip` | ZIP archive containing a Shapefile (`.shp`, `.shx`, `.dbf`, `.prj`). |
    | `.kml` | Keyhole Markup Language. Fully supported. |

    4. Click **Save**. Processing begins automatically.

    ## 7.5 Monitoring File Processing

    Status: `Created → Processing → Ready` (or `Error`). If a file enters Error state, open the record and read the **Error Message**. Use **Reprocess files** to re-queue.

    ## 7.6 Publishing a Dataset

    Only superusers can publish datasets. Select datasets in the list view and use the **Actions** dropdown:

    | Action | Effect |
    |---|---|
    | Make dataset public | Sets `is_public = True` |
    | Make dataset private | Sets `is_public = False` |
    | Publish dataset | Sets `is_approved = True` |
    | Unpublish dataset | Sets `is_approved = False` |

    :::note Visibility rule
    A dataset is visible to unauthenticated users only when both `is_public = True` AND `is_approved = True`. Authenticated users can see any dataset where `is_approved = True`, regardless of `is_public`.
    :::
""")

f("docs/backend/08-raster-datasets.md", """
    ---
    sidebar_position: 8
    title: "8. Raster Datasets & Raster Files"
    ---

    # 8. Raster Datasets and Raster Files

    Raster Datasets store georeferenced imagery (satellite photos, terrain models, derived raster outputs). They are displayed as Cloud-Optimized GeoTIFF (COG) layers. Unlike vector data, raster files do not require PMTiles conversion — they are served directly from object storage.

    ## 8.1 Adding a Raster Dataset

    1. Go to **Datasets → Raster Datasets → + Add Raster Dataset**.
    2. Fill in the same metadata fields as Vector Datasets (name, description, source, contact, CRS, etc.). Supports EN/PT translations.
    3. Click **Save**. Then add a Raster File.

    ## 8.2 Adding Raster Files

    1. Go to **Datasets → Raster Files → + Add Raster File**.
    2. Select the parent Raster Dataset.
    3. Upload a raster file. Accepted formats: `.tiff`, `.tif`, `.geotiff`, `.gtiff`, `.vrt`.
    4. Click **Save**.

    :::warning COG requirements
    For best performance, raster files must be Cloud-Optimized GeoTIFFs in **EPSG:3857** with **256×256 block size** and the Google Maps tiling scheme.

    **Single-band data:**
    ```bash
    gdalwarp <source.tif> <dest.tif> -of COG -t_srs EPSG:3857 \\
      -co BLOCKSIZE=256 -co TILING_SCHEME=GoogleMapsCompatible
    ```

    **RGB imagery (satellite):**
    ```bash
    gdalwarp <source.tif> <dest.tif> -of COG -t_srs EPSG:3857 \\
      -co BLOCKSIZE=256 -co TILING_SCHEME=GoogleMapsCompatible \\
      -co COMPRESS=JPEG -co ADD_ALPHA=NO -dstnodata NaN
    ```
    :::

    ## 8.3 Linking Raster Datasets to Data Models

    Add a Raster Dataset to a Data Model's **Raster Layers** multi-select to make it available as an optional map layer in the explorer. Only approved Raster Datasets appear in this selector.
""")

f("docs/backend/09-reference-datasets.md", """
    ---
    sidebar_position: 9
    title: "9. Reference Datasets & Reference Files"
    ---

    # 9. Reference Datasets and Reference Files

    Reference Datasets store non-spatial supporting documents and tabular files — methodology reports, data dictionaries, Excel tables, PDFs — that provide context for the energy planning analysis. They appear in the Downloads section of the frontend.

    ## 9.1 Adding a Reference Dataset

    1. Go to **Datasets → Reference Datasets → + Add Reference Dataset**.
    2. Fill in the metadata fields (name, description, source, contact, etc.). Supports EN/PT translations.
    3. Click **Save**. Then add Reference Files.

    ## 9.2 Adding Reference Files

    1. Go to **Datasets → Reference Files → + Add Reference File**.
    2. Select the parent Reference Dataset.
    3. Upload a file. Accepted formats: `.pdf`, `.csv`, `.xlsx`, `.xls`, `.docx`, `.doc`.
    4. Click **Save**.

    ## 9.3 Linking Reference Datasets to Data Models

    Add a Reference Dataset to a Data Model's **Reference Datasets** multi-select to associate it with that model's analysis context. The documents then appear in the Downloads section, filterable by model.
""")

f("docs/backend/10-monitoring.md", """
    ---
    sidebar_position: 10
    title: "10. Monitoring & Troubleshooting"
    ---

    # 10. Monitoring and Troubleshooting

    ## 10.1 Monitoring Background Tasks

    - **In Django Admin:** Go to **Django Celery Results → Task Results** to see all completed, failed, and pending tasks.
    - **Via Flower (local dev):** Run `celery -A proenergia flower --address=127.0.0.1 --port=5555` and access `http://localhost:5555`.

    ## 10.2 Admin Troubleshooting

    | Issue | Cause & Resolution |
    |---|---|
    | VectorFile stuck in Processing | Celery worker is not running. Restart: `sudo systemctl restart proenergia-celery` |
    | VectorFile / ScenarioFile shows Error | Open the record and read the **Error Message**. Common causes: unsupported CRS, corrupt file, or CSV missing the `id` column. |
    | `filter_fields` fails: Missing a required key | Each entry must have all three keys: `label`, `description`, `column`. |
    | `summary_fields` fails: columns key should be a list | The `columns` key must be a JSON array even for one column: `["MyColumn"]` |
    | `summary_fields` fails: invalid chartType | Valid values: `bar`, `donut`, `stacked`, `column`, `area`, `highlight`. |
    | `color_coding` fails: invalid color | Each color must be a valid 3 or 6-digit hex code (e.g. `#FF0000`). |
    | Frontend shows no features (blank map) | The Scenario's ScenarioFile must be in Ready status. Check file processing. |
    | Summary panel shows all zeros | `metric_field_types` may not be populated. It auto-populates on successful Scenario File import. |
    | Admin login shows 403 | User exists but lacks Staff status. A Super Admin must enable it. |
    | Model not visible on frontend | Data Model's `is_public` flag is `False`. Only superusers can see private models. |
""")

f("docs/backend/11-api-reference.md", """
    ---
    sidebar_position: 11
    title: "11. API Reference"
    ---

    # 11. API Reference

    - **Base URL:** `/api/v1/`
    - **Swagger docs:** `/api/v1/docs/`
    - **OpenAPI schema:** `/api/v1/schema/`

    ## Endpoints

    | Endpoint | Description |
    |---|---|
    | `GET /api/v1/model/` | List all public Data Models. Non-superusers see only `is_public=True` models. Returns `filter_fields`, `popup_fields`, `summary_fields`, `color_coding`, `metric_field_types`, `scenarios`, `name_pt`, `description_pt`, `presentation_order`. |
    | `GET /api/v1/model/{id}/` | Retrieve a single Data Model by ID. |
    | `GET /api/v1/vector/` | List VectorDatasets. Public+approved for anonymous; all approved for authenticated; all for superusers. |
    | `GET /api/v1/vector/{id}/` | Retrieve a single VectorDataset. |
    | `GET /api/v1/raster/` | List RasterDatasets. Same visibility rules as vector datasets. |
    | `GET /api/v1/raster/{id}/` | Retrieve a single RasterDataset. |
    | `GET /api/v1/reference/` | List ReferenceDatasets. Same visibility rules as vector datasets. |
    | `GET /api/v1/reference/{id}/` | Retrieve a single ReferenceDataset. |
    | `GET /api/v1/scenario/{id}/feature/{feature_id}/` | Retrieve all stored metadata for a single feature. Used to populate map popups. |
    | `GET /api/v1/scenario/{id}/summaries/` | Compute statistical summaries. See Section 11.1. |
    | `DELETE /api/v1/scenario/{id}/summaries/cache/` | Purge cached summary responses for a scenario. |
    | `POST /api/v1/token-auth/` | Obtain an authentication token. Body: `{"username": "...", "password": "..."}` |

    ## 11.1 Summaries Endpoint

    `GET /api/v1/scenario/{id}/summaries/`

    | Parameter | Description |
    |---|---|
    | `fields` (required) | Comma-separated column names to aggregate. E.g. `fields=Pop2030,Technology2030` |
    | `q` (optional) | Filter expression. Comma-separated conditions: `field=value` (equality); `field__min=N` and `field__max=N` (numeric range); `field__in=val1;val2` (multi-value string). |
    | `group_by` (optional) | Comma-separated string-type column name(s). Must be in `metric_field_types`. Maximum 2 fields for nested grouping. |

    ### Filter Examples

    ```bash
    # Single value match
    ?fields=Pop2030&q=Technology2030=SHS

    # Numeric range
    ?fields=InvestmentCostTotal&q=Pop2030__min=100,Pop2030__max=5000

    # Multi-value string filter
    ?fields=Pop2030&q=Technology2030__in=SHS;MiniGrid

    # With grouping
    ?fields=Pop2030&q=Admin_1=Maputo&group_by=Technology2030

    # Two-level nested grouping
    ?fields=Pop2030&group_by=Admin_1,Technology2030
    ```

    ### Response Structure

    ```json
    {
      "scenario_id": 1,
      "filters_applied": "Admin_1=Maputo",
      "summaries": {
        "Pop2030": {
          "type": "numeric",
          "count": 7354,
          "min": 3.69,
          "max": 3620782.55,
          "sum": 4466719.88
        },
        "Technology2030": {
          "type": "string",
          "count": 7354,
          "values": { "SHS": 2100, "MiniGrid": 850, "Grid": 4404 }
        }
      }
    }
    ```

    :::note Caching
    Summary responses are cached for 24 hours. Use `DELETE /summaries/cache/` after uploading new Scenario File data.
    :::
""")


# ══════════════════════════════════════════════════════════════════════════
# FRONTEND
# ══════════════════════════════════════════════════════════════════════════

f("docs/frontend/12-interface-overview.md", """
    ---
    sidebar_position: 12
    title: "12. Interface Overview"
    ---

    # 12. Frontend Interface Overview

    ## 12.1 Getting Started

    The PROENERGIA+ visualization interface is a web application — no installation required. It runs in any modern browser (Chrome, Firefox, Edge, or Safari).

    | Access Level | What you can do |
    |---|---|
    | **Public (unauthenticated)** | View and explore all public, approved Data Models. Apply filters, view popups, download public data. |
    | **Authenticated User** | Access all public datasets plus any private approved datasets. Full visualization and download capabilities. |

    ## 12.2 Language Selection

    The platform supports **English** and **Portuguese** (default). To switch languages, click the **PT / EN** toggle in the top-right of the header. Your preference is saved in the browser and persists across sessions.

    Translated content includes: navigation labels, filter labels, scenario names, model names, layer names, and all UI strings. Portuguese translations come from:
    - Locale JSON files for UI strings
    - The `name_pt` / `description_pt` fields set on Data Models, Scenarios, and Datasets in the admin

    ## 12.3 Three-Panel Layout

    | Panel | Location / Function |
    |---|---|
    | **Model Navigation Sidebar** | Far left. Lists all public Data Models with unique icons, ordered by Presentation Order. Click any icon to activate that model. |
    | **Filter / Control Panel** | Left panel. Contains the scenario selector and all filter controls. Can be collapsed using the toggle button on its right edge. |
    | **Map Panel** | Centre. Interactive MapLibre GL map displaying the active scenario's PMTiles vector layer. |
    | **Analysis Summary Panel** | Right. Displays aggregated statistics for the current scenario and active filters. Also shows feature detail when a map feature is clicked. |
""")

f("docs/frontend/13-model-navigation.md", """
    ---
    sidebar_position: 13
    title: "13. Model Navigation & Scenario Selection"
    ---

    # 13. Model Navigation and Scenario Selection

    ## 13.1 Switching Between Data Models

    The leftmost sidebar lists all public Data Models as icon buttons, ordered by their **Presentation Order** field. Click any icon to activate the model — all three panels update. A model switcher menu is also available in the control panel header for quick switching.

    ## 13.2 Selecting a Scenario

    The scenario dropdown near the top of the Filter Panel lists all available scenarios for the active model, ordered by **Presentation Order**. Only scenarios with a ScenarioFile in **Ready** status appear.

    The selected scenario is encoded in the URL (`?scenario=...`) for bookmarking and sharing.
""")

f("docs/frontend/14-filter-panel.md", """
    ---
    sidebar_position: 14
    title: "14. The Filter Panel"
    ---

    # 14. The Filter Panel

    ## 14.1 Overview

    The Filter Panel contains all filter controls defined in the Data Model's `filter_fields` configuration. Filters simultaneously narrow the features displayed on the map and update the Analysis Summary statistics.

    ## 14.2 Administrative Area Filters

    Geographic filters are rendered as searchable multi-select **Combobox** controls for columns matching administrative geography keywords. The Mozambique administrative hierarchy:

    - **Province** (Província / Região)
      - **District** (Distrito)
        - **Administrative Post** (Posto Administrativo)
          - **Locality** (Localidade)

    ## 14.3 Technology / Category Filters

    **Checkbox** filters are shown for string-valued columns. By default all values are selected (visible). Uncheck any value to hide features with that value. Values are colour-coded consistently with the map legend.

    ## 14.4 Numeric Range Filters

    **Dual text-input range** controls are shown for numeric columns. Enter a minimum and/or maximum to restrict the displayed features.

    Common uses: Settlement Population, Investment Cost, Distance to Grid.

    :::tip
    Combine range filters with technology checkboxes — e.g. all mini-grid sites with population over 1,000 and investment cost under $500,000.
    :::

    ## 14.5 Applying and Clearing Filters

    Filter changes are **staged**. A visual indicator on each filter shows pending or active (changed from default) state.

    - Click **Apply** to commit all pending changes.
    - Click **Reset** to clear all filters to their defaults.

    Applied filter state is encoded in the URL for bookmarking and sharing.
""")

f("docs/frontend/15-map-panel.md", """
    ---
    sidebar_position: 15
    title: "15. The Map Panel"
    ---

    # 15. The Map Panel

    ## 15.1 Map Controls and Navigation

    | Control | Description |
    |---|---|
    | Zoom | Scroll wheel, pinch gesture, or the +/- buttons. |
    | Pan | Click and drag. |
    | Re-centre | Click the re-centre button (bottom right) to return to the default Mozambique extent. |
    | **Geocoder (address search)** | Search bar in the top-left. Search for place names via OpenStreetMap Nominatim. Matching locations are shown with a marker. |
    | **Share button** | Copies the current page URL (including all active filters and scenario) to the clipboard for sharing. |

    ## 15.2 Map Controls Toolbar

    | Control | Description |
    |---|---|
    | **Basemap selector** | Switch between light, dark, and other available basemap styles. |
    | **Opacity control** | Adjust the opacity of the active scenario's data layer. |
    | **Legend** | Colour key for the active visualization column. Corresponds to the `color_coding` configuration. |
    | **Contextual layer panel** | Toggle individual vector layers (from Data Model's Contextual Layers) on/off. |
    | **Raster layer panel** | Toggle individual raster layers (from Data Model's Raster Layers) on/off as additional map overlays. |

    ## 15.3 Feature Interaction

    Clicking a feature on the map switches the right-hand panel to **feature detail mode**, showing the attributes configured in `popup_fields`.

    The panel header shows the feature identifier. Click the **back arrow** to return to the national summary view.
""")

f("docs/frontend/16-summary-panel.md", """
    ---
    sidebar_position: 16
    title: "16. The Analysis Summary Panel"
    ---

    # 16. The Analysis Summary Panel

    ## 16.1 Overview

    The Analysis Summary Panel displays aggregated statistics that update in real time when filters are applied. All statistics correspond to entries in the Data Model's `summary_fields` configuration.

    ## 16.2 Statistics Display Formats

    | Display type | When shown |
    |---|---|
    | **Single value (flat)** | Single column, no `group_by`, no `chartType`. Shows the computed value with optional unit. |
    | **Group breakdown** | `group_by` set but no `chartType`. Shows value per group as a labelled list. |
    | **Chart** (bar/donut/stacked/column/area) | `chartType` set. Shows an interactive chart. `showChartValueRows: true` adds a table beneath. |
    | **Highlight** | `chartType: "highlight"`. Shows a prominent single-value highlight card. |
    | **Multi-column group** | `columns` has multiple entries. Each column is a sub-row aggregated by `method`. |
    | **Nested group** | `group_by` set to two columns. Shows a two-level grouped breakdown. |

    ## 16.3 Summary Categories

    Items sharing the same `category` value are grouped under a collapsible heading in the summary panel.
""")

f("docs/frontend/17-downloads.md", """
    ---
    sidebar_position: 17
    title: "17. Downloads"
    ---

    # 17. Downloads

    The Downloads page (accessible from the header navigation) lists all Vector Datasets, Raster Datasets, and Reference Datasets you have access to. Unauthenticated users see only public, approved datasets.

    Each card shows the name, description, source attribution, and last updated date. Click **Download** to download the raw source file in its original format.

    Use the search box at the top to filter datasets by name or description.

    :::note
    Downloads of vector data reflect the **original uploaded file** (GeoJSON, GeoPackage, Shapefile, or KML), not the processed PMTiles. Load them directly into QGIS, ArcGIS, or similar tools.
    :::
""")

f("docs/frontend/18-content-pages.md", """
    ---
    sidebar_position: 18
    title: "18. Content & Documentation Pages"
    ---

    # 18. Content and Documentation Pages

    ## 18.1 MDX-Based Content System

    The platform includes static documentation pages authored in **MDX** (Markdown with embedded React components). These pages support bilingual content via locale-specific MDX files.

    **File naming convention:**

    ```
    src/app/<page>/<slug>.mdx       # English (default)
    src/app/<page>/<slug>.pt.mdx    # Portuguese
    ```

    The correct file is served automatically based on the user's selected language.

    **Currently available pages:**

    | Page | English | Portuguese |
    |---|---|---|
    | `/about` | `src/app/about/about.mdx` | `src/app/about/about.pt.mdx` |

    To add or update content pages, a developer must edit the `.mdx` files in the repository and redeploy. Non-developer administrators should coordinate with Development Seed for content updates.
""")

f("docs/frontend/19-troubleshooting.md", """
    ---
    sidebar_position: 19
    title: "19. Frontend Troubleshooting"
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
""")


# ══════════════════════════════════════════════════════════════════════════
# DEPLOYMENT
# ══════════════════════════════════════════════════════════════════════════

f("docs/deployment/20-server-requirements.md", """
    ---
    sidebar_position: 20
    title: "20. Server Requirements"
    ---

    # 20. Server Requirements and Prerequisites

    **OS:** Ubuntu 24.04 LTS (recommended). Minimum 4 GB RAM; 16 GB+ recommended for production.

    | Requirement | Details |
    |---|---|
    | Domain | A registered domain name with DNS pointing to the server's public IP. |
    | Python | 3.12+ (installed by setup script). |
    | PostgreSQL 16 + PostGIS | Database. PostGIS required for spatial queries. |
    | RabbitMQ | Message broker for Celery. |
    | GDAL / gdal-bin | Geospatial file format conversion (`ogr2ogr`). |
    | Tippecanoe | PMTiles generation from vector data. |
    | Nginx | Web server / reverse proxy. |
    | Certbot | Let's Encrypt SSL certificate management. |

    All requirements are installed automatically by the setup scripts.
""")

f("docs/deployment/21-deployment-overview.md", """
    ---
    sidebar_position: 21
    title: "21. Deployment Overview"
    ---

    # 21. Deployment Overview: Five-Script Process

    The `deploy/scripts/` directory contains five numbered shell scripts that automate the full deployment. Run them in order.

    ## Quick Start

    ```bash
    git clone https://github.com/developmentseed/moz-proenergia-backend.git
    cd moz-proenergia-backend/deploy/scripts
    chmod +x *.sh

    ./00_setup_system.sh
    ./01_setup_infrastructure.sh your-domain.com       # DOMAIN REQUIRED
    sudo -u proenergia ./02_setup_application.sh
    ./03_setup_services.sh your-domain.com admin@email  # DOMAIN + optional email
    ./04_verify_setup.sh
    ```

    ## Script Reference

    | Script | Run as | Purpose |
    |---|---|---|
    | `00_setup_system.sh` | root | Install system packages (Python, PostgreSQL 16+PostGIS, RabbitMQ, Nginx, Certbot, Tippecanoe, GDAL). Create `proenergia` system user and application directories. |
    | `01_setup_infrastructure.sh <domain>` | root | Configure PostgreSQL (DB, user, PostGIS + pg_trgm + unaccent extensions, optimize settings). Configure RabbitMQ (dedicated user + vhost). Generate Django secret key. Write complete `.env` file to `/var/www/proenergia/app/.env`. **Save the displayed credentials.** |
    | `02_setup_application.sh` | proenergia user | Clone repo to `/var/www/proenergia/app`. Create Python virtualenv, install requirements. Run `migrate`, `createcachetable`, `collectstatic`, `compilemessages`. |
    | `03_setup_services.sh <domain> [email]` | root | Install nginx config, Gunicorn service, Celery services, webhook listener. Generate webhook secret. Install SSL via certbot. Configure firewall. Start all services. |
    | `04_verify_setup.sh` | any | Verify all services running, database connection, file permissions, web accessibility. Prints pass/fail summary. |

    :::warning Order matters
    Scripts must be run in sequence. Script `01` generates the `.env` file that script `02` requires. Script `02` installs the application files that script `03` configures.
    :::

    ## File Locations

    | Path | Description |
    |---|---|
    | `/var/www/proenergia/app/` | Application root |
    | `/var/www/proenergia/app/.env` | Environment configuration (chmod 600) |
    | `/var/www/proenergia/app/staticfiles/` | Collected static files |
    | `/var/www/proenergia/app/media/` | Uploaded files and PMTiles |
    | `/var/log/proenergia/` | Application logs |
    | `/etc/nginx/sites-available/proenergia.conf` | Nginx configuration |
    | `/etc/systemd/system/proenergia*.service` | systemd service files |
""")

f("docs/deployment/22-environment-configuration.md", """
    ---
    sidebar_position: 22
    title: "22. Environment Configuration"
    ---

    # 22. Environment Configuration

    The `.env` file is automatically generated by script `01` and placed at `/var/www/proenergia/app/.env`. Key variables:

    | Variable | Description |
    |---|---|
    | `DJANGO_SECRET_KEY` | Auto-generated Django secret key. Never share or commit. |
    | `DJANGO_DEBUG` | Set to `False` in production. |
    | `DATABASE_URL` | PostGIS connection string. Format: `postgis://user:password@localhost:5432/proenergia_db` |
    | `ALLOWED_HOSTS` | Comma-separated allowed hostnames (your domain and www subdomain). |
    | `CSRF_TRUSTED_ORIGINS` | Comma-separated trusted origins for CSRF protection. |
    | `STATIC_ROOT` | Filesystem path where `collectstatic` writes static files. |
    | `MEDIA_ROOT` | Filesystem path where uploaded files and PMTiles are stored. |
    | `CELERY_BROKER_URL` | RabbitMQ connection: `amqp://proenergia:<password>@localhost:5672/proenergia_vhost` |
    | `CELERY_WORKERS` | Number of Celery worker processes (default: 2). |
    | `CELERY_WORKER_CONCURRENCY` | Concurrency per worker (default: 4). |
    | `CACHE_BACKEND` | Database cache backend: `django.core.cache.backends.db.DatabaseCache` |
    | `CACHE_LOCATION` | Cache table name: `summaries_cache_table` |

    :::warning Security
    The `.env` file has permissions `600` (owner read/write only). Never commit it to version control.
    :::

    :::note Database name
    The production database is named `proenergia_db` (not `proenergia`). The RabbitMQ vhost is `proenergia_vhost`. These differ from a typical local development setup.
    :::
""")

f("docs/deployment/23-post-installation.md", """
    ---
    sidebar_position: 23
    title: "23. Post-Installation Setup"
    ---

    # 23. Post-Installation Setup

    ## 23.1 Create Django Admin Superuser

    ```bash
    cd /var/www/proenergia/app
    source venv/bin/activate
    python manage.py createsuperuser
    ```

    ## 23.2 Configure GitHub Webhook (Optional)

    Script `03` generates a webhook secret displayed at the end of its output (also saved to `/var/www/proenergia/webhook_secret.txt`).

    1. Go to **GitHub repository → Settings → Webhooks → Add webhook**.
    2. Set **Payload URL** to `https://your-domain.com/deploy-webhook`.
    3. Set **Content type** to `application/json`.
    4. Paste the webhook secret into the **Secret** field.
    5. Select **Just the push event**. Click **Add webhook**.

    ## 23.3 systemd Services

    | Service | Purpose |
    |---|---|
    | `proenergia.service` | Gunicorn WSGI application server. Serves the Django REST API. |
    | `proenergia-celery.service` | Celery worker. Processes PMTiles generation and CSV import tasks. |
    | `proenergia-celerybeat.service` | Celery Beat scheduler. Handles periodic/scheduled tasks. |
    | `proenergia-webhook.service` | Webhook listener for automated git-push deployments. |

    ```bash
    # Status and logs
    sudo systemctl status proenergia
    sudo journalctl -u proenergia -f
    sudo journalctl -u proenergia-celery -f

    # Restart after changes
    sudo systemctl restart proenergia
    sudo systemctl restart proenergia-celery
    sudo systemctl restart proenergia-celerybeat
    ```
""")

f("docs/deployment/24-update-procedures.md", """
    ---
    sidebar_position: 24
    title: "24. Update Procedures"
    ---

    # 24. Update Procedures

    ## 24.1 Manual Update

    ```bash
    # Run as the proenergia user
    sudo -u proenergia /var/www/proenergia/app/deploy/scripts/05_update_app.sh

    # Or use the installed command (requires sudoers config from script 03)
    sudo deploy-proenergia
    ```

    The update script (`05_update_app.sh`) performs these steps in order:

    1. `git pull origin main`
    2. Activate virtualenv and `pip install -r requirements.txt --upgrade`
    3. `python manage.py migrate`
    4. `python manage.py createcachetable`
    5. `python manage.py collectstatic --noinput`
    6. `python manage.py compilemessages -f`

    :::warning
    Always run migrations **before** restarting the application after a code update that contains schema changes.
    :::

    ## 24.2 Rollback

    ```bash
    cd /var/www/proenergia/app
    git log --oneline -5            # find previous commit
    git checkout <previous-commit>
    sudo systemctl restart proenergia
    sudo systemctl restart proenergia-celery
    ```

    ## 24.3 Verification After Update

    ```bash
    # Health check (with retry loop)
    bash /var/www/proenergia/app/deploy/scripts/health-check.sh --wait

    # Full verification suite
    bash /var/www/proenergia/app/deploy/scripts/04_verify_setup.sh

    # Manual API check
    curl https://your-domain.com/api/v1/model/
    ```
""")

f("docs/deployment/25-backup-recovery.md", """
    ---
    sidebar_position: 25
    title: "25. Backup & Recovery"
    ---

    # 25. Backup and Recovery

    ## 25.1 Database Backup

    ```bash
    # Backup
    sudo -u postgres pg_dump proenergia_db > backup_$(date +%Y%m%d).sql

    # Restore
    sudo -u postgres psql proenergia_db < backup_20240101.sql
    ```

    ## 25.2 Media Files Backup

    ```bash
    # Backup all uploaded files and PMTiles
    tar -czf media_backup_$(date +%Y%m%d).tar.gz /var/www/proenergia/app/media/

    # Backup the environment config
    cp /var/www/proenergia/app/.env ~/env_backup_$(date +%Y%m%d)
    ```

    ## 25.3 PostgreSQL Performance Tuning

    Script `01` automatically applies PostgreSQL optimizations based on system RAM: `shared_buffers`, `work_mem`, `maintenance_work_mem`, `effective_cache_size`, `max_connections`, checkpoint settings, and autovacuum parameters.

    To monitor slow queries:

    ```sql
    SELECT query, total_exec_time, calls
    FROM pg_stat_statements
    ORDER BY total_exec_time DESC
    LIMIT 10;
    ```
""")

f("docs/deployment/26-troubleshooting.md", """
    ---
    sidebar_position: 26
    title: "26. Deployment Troubleshooting"
    ---

    # 26. Deployment Troubleshooting

    | Issue | Cause & Resolution |
    |---|---|
    | 502 Bad Gateway from Nginx | Gunicorn not running. Check: `sudo systemctl status proenergia`. View logs: `sudo journalctl -u proenergia -n 50` |
    | PMTiles not generating | Celery worker not running. Check: `sudo systemctl status proenergia-celery`. Also verify RabbitMQ: `sudo rabbitmqctl status` |
    | Connection refused to RabbitMQ | RabbitMQ stopped. Run: `sudo systemctl start rabbitmq-server` |
    | Database connection errors | Check `DATABASE_URL` in `.env`. Verify PostgreSQL: `sudo systemctl status postgresql` |
    | Settings import errors at startup | `DJANGO_SECRET_KEY` is not set. Verify `.env` exists and is readable by the `proenergia` user. |
    | Static files returning 404 | Run: `python manage.py collectstatic --noinput`. Verify Nginx serves the `STATIC_ROOT` path. |
    | Migrations fail on restart | Run `migrate` manually and check for errors before restarting services. |
    | Translation errors (compilemessages) | `gettext` tools may be missing. Install: `sudo apt install gettext`. Then rerun `compilemessages`. |
    | SSL certificate issues | Run: `sudo certbot renew --dry-run`. Check Nginx config: `sudo nginx -t` |
    | Webhook not triggering | Check: `sudo systemctl status proenergia-webhook`. View secret: `sudo cat /var/www/proenergia/webhook_secret.txt`. Check GitHub webhook delivery logs. |
    | Database cache table missing | Run: `python manage.py createcachetable`. The table `summaries_cache_table` must exist for the application to start. |
""")


# ══════════════════════════════════════════════════════════════════════════
# APPENDICES
# ══════════════════════════════════════════════════════════════════════════

f("docs/appendices/a-json-skeletons.md", """
    ---
    sidebar_position: 100
    title: "Appendix A — JSON Skeletons"
    ---

    # Appendix A — Complete JSON Skeletons

    ## `filter_fields`

    ```json
    [
      {
        "label":          "Human-readable label",
        "description":    "Tooltip text (or empty string)",
        "column":         "CSV_Column_Name",
        "label_pt":       "Rótulo em Português",
        "description_pt": "Descrição em Português"
      }
    ]
    ```

    ## `popup_fields`

    ```json
    [
      {
        "label":          "Human-readable label",
        "description":    "Tooltip text (or empty string)",
        "column":         "CSV_Column_Name",
        "label_pt":       "Rótulo em Português",
        "description_pt": "Descrição em Português"
      }
    ]
    ```

    ## `summary_fields`

    ```json
    [
      {
        "label":               "Display heading",
        "description":         "Tooltip (or empty string)",
        "columns":             ["CSV_Column_Name"],
        "method":              "sum",
        "unit":                "USD",
        "group_by":            "OtherColumn",
        "category":            "Section Heading",
        "chartType":           "bar",
        "colors":              { "Value": "#HEX" },
        "hasDecimal":          false,
        "showChartValueRows":  false,
        "showBarChartAverage": false,
        "label_pt":            "Rótulo em Português",
        "description_pt":      "Descrição em Português"
      }
    ]
    ```

    `method` values: `sum` | `average` | `count` | `min` | `max`

    `chartType` values: `bar` | `donut` | `stacked` | `column` | `area` | `highlight`

    ## `color_coding`

    ```json
    [
      { "value": "DataValue1", "color": "#RRGGBB" },
      { "value": "DataValue2", "color": "#RRGGBB" },
      { "value": "default",   "color": "#RRGGBB" }
    ]
    ```
""")

f("docs/appendices/b-admin-columns.md", """
    ---
    sidebar_position: 101
    title: "Appendix B — Admin Column Keywords"
    ---

    # Appendix B — Administrative Column Keywords

    Columns with these **exact names** (case-sensitive) are rendered as searchable multi-select Combobox controls rather than checkboxes or range controls:

    ```
    Admin_1, Admin_2, Admin_3, Admin_4
    Region, Regions, Região, Regiões
    Province, Provinces, Província, Províncias
    District, Districts, Distrito, Distritos
    Posto, Postos
    Localidade, Localidades
    ```

    :::warning
    Column names are matched exactly and case-sensitively. A column named `"province"` (lowercase) will **not** be treated as an admin filter — use `"Province"`.
    :::
""")

f("docs/appendices/c-permissions.md", """
    ---
    sidebar_position: 102
    title: "Appendix C — Permissions Matrix"
    ---

    # Appendix C — Permissions Matrix Summary

    | Action | User | Admin | Super Admin |
    |--------|:----:|:-----:|:-----------:|
    | **VIEW & DOWNLOAD** | | | |
    | View & explore public Data Models (frontend) | ✓ | ✓ | ✓ |
    | View private Data Models (frontend / API) | — | — | ✓ |
    | Download public datasets | ✓ | ✓ | ✓ |
    | Download private datasets | — | ✓ | ✓ |
    | **BACKEND ADMINISTRATION** | | | |
    | Access Django Admin interface | — | ✓ | ✓ |
    | Upload vector / raster / reference files | — | ✓ | ✓ |
    | Edit Data Model JSON configuration | — | ✓ | ✓ |
    | Set Data Model `is_public` flag | — | — | ✓ |
    | Add / edit Scenarios and Scenario Files | — | ✓ | ✓ |
    | Publish / unpublish datasets (`is_approved`) | — | — | ✓ |
    | Set `is_public` flag on datasets | — | — | ✓ |
    | Delete any data record | — | — | ✓ |
    | Create and manage user accounts | — | — | ✓ |
""")

f("docs/appendices/d-glossary.md", """
    ---
    sidebar_position: 103
    title: "Appendix D — Glossary"
    ---

    # Appendix D — Glossary

    | Term | Definition |
    |---|---|
    | **Data Model** | A thematic analysis category (e.g., Least Cost Electrification). Container and configuration for Scenarios, Vector Datasets, and display settings. Can be public or private (`is_public`). |
    | **Scenario** | A specific model run within a Data Model (e.g., Baseline 2025). Linked to a Vector Dataset and one or more Scenario Files. Ordered by `presentation_order`. |
    | **Scenario File** | A CSV uploaded to a Scenario containing modeled output attributes. Must include an `id` column. Supports `low_zoom_as_points` rendering option. |
    | **ScenarioData** | Database table (JSONB) storing all imported Scenario File attribute data per feature. Powers the `/feature/` API endpoint. |
    | **ScenarioDataMetrics** | Denormalized key-value table for fast aggregation queries. Auto-populated on Scenario File import. Powers the `/summaries/` API endpoint. |
    | **Vector Dataset** | Named container for spatial geometry files (`.geojson`, `.gpkg`, `.zip`, `.kml`). Includes rich metadata fields. Supports EN/PT translations. |
    | **Raster Dataset** | Container for Cloud-Optimized GeoTIFF (COG) imagery files. Displayed as raster overlay layers on the map. |
    | **Reference Dataset** | Container for supporting documents and tables (`.pdf`, `.csv`, `.xlsx`, `.docx`, etc.). Listed in the Downloads section. |
    | **PMTiles** | Single-file vector tile archive served via HTTP range requests. Generated from vector files using Tippecanoe. |
    | **COG** | Cloud-Optimized GeoTIFF. A raster format optimised for streaming from object storage. Must be in EPSG:3857 with 256×256 block size for the platform's raster rendering. |
    | **presentation_order** | Integer field on DataModel and Scenario controlling sort order in the frontend sidebar and dropdown. Lower numbers appear first. |
    | **is_public (DataModel)** | Boolean on DataModel. If `False`, the model is hidden from the API for non-superusers and does not appear on the frontend. |
    | **metric_field_types** | JSON dict on DataModel mapping CSV column names to `"numeric"` or `"string"`. Auto-populated on Scenario File import. Powers the summaries API. |
    | **visualization_column** | The CSV column whose unique values determine map feature colours, as configured by `color_coding`. |
    | **low_zoom_as_points** | ScenarioFile option that renders polygon centroids at low zoom (5–10) and full geometry at high zoom (11–14). Improves performance for large polygon datasets. |
    | **Celery** | Distributed task queue for async processing (PMTiles generation, CSV import). |
    | **RabbitMQ** | Message broker for Celery. In production, uses a dedicated vhost: `proenergia_vhost`. |
    | **Tippecanoe** | Command-line tool that generates PMTiles from FlatGeobuf vector data. |
    | **tile-join** | Tippecanoe companion tool that merges multiple PMTiles files (used for `low_zoom_as_points`). |
    | **GDAL / ogr2ogr** | Geospatial data library for format conversion and reprojection. |
    | **i18n** | Internationalisation. The platform supports Portuguese (default) and English via i18next. Backend models support `name_pt` and `description_pt` translation fields. |
    | **proenergia_db** | The production PostgreSQL database name. |
    | **DATABASE_URL** | Primary environment variable for the database connection (`postgis://...`). |
""")


# ══════════════════════════════════════════════════════════════════════════
# WRITE
# ══════════════════════════════════════════════════════════════════════════
write_all()

print("\nNext steps:")
print(f"  cd {OUT}")
print("  npm install")
print("  npm start")