# ODOO19-Report Theme Manager
Odoo 19 module to manage multi-theme profiles for QWeb PDF reports with RTL support

# Report Theme Manager

An Odoo 19 module that lets you create and manage multiple branding theme profiles for your PDF reports. Instead of hardcoding colors and fonts into each report template, you define named theme profiles and assign them per company — one place, all reports.

Built because most clients ask for branded reports on day one, and Odoo's built-in document layout only gets you so far.

---

## What it does

- Create unlimited theme profiles with custom colors, fonts, header/footer content
- Assign a different theme per company
- Supports RTL layout for Arabic and Urdu reports (with fonts like Tajawal, Cairo, Amiri)
- Add watermarks (DRAFT, PAID, CONFIDENTIAL, or any custom text) with configurable opacity
- Apply themes selectively — Invoice only, Sale Orders only, or all three
- Switch the active theme from the Settings screen in one click

Covers Invoice, Sale Order, and Purchase Order reports out of the box.

---

## Why this exists

Odoo 19 has a built-in Document Layout config under Settings. It covers logo, colors, and font — but it's global. There's no way to:

- Save multiple named themes and switch between them
- Assign different themes per report type
- Enable RTL layout with the right Arabic font
- Add a watermark dynamically based on document state

This module fills those gaps.

---

## Installation

1. Clone or download this repo into your Odoo `custom_addons` folder:

```bash
git clone https://github.com/umarahmadrafi008/odoo19-report-theme-manager.git report_theme_manager
```

2. Make sure the folder is named `report_theme_manager` (no hyphens — Odoo doesn't accept them in module names)

3. Add the path to your `odoo.conf`:

```
addons_path = ..., /path/to/your/custom_addons
```

4. Restart Odoo, go to **Apps → Update App List**, search for `Report Theme Manager`, and install.

---

## How to use

**Create a theme:**

Go to **Report Themes → Theme Profiles → New**

Fill in the tabs:
- **Branding** — primary/secondary colors, font family, font sizes
- **Header & Footer** — toggle on/off, add custom HTML content (supports Arabic text)
- **RTL & Arabic** — enable right-to-left layout and pick an Arabic font
- **Watermark** — enable, set text and opacity
- **Apply To** — choose which reports this theme affects

**Activate a theme:**

Go to **Settings → Report Themes** and select the theme from the dropdown. It applies immediately to all PDF reports for that company.

---

## Compatibility

| Odoo Version | Status |
|---|---|
| 19.0 | ✅ Tested |
| 18.0 | Not tested |
| 17.0 | Not tested |

---

## Module structure

```
report_theme_manager/
├── models/
│   ├── report_theme_profile.py   # Core theme model with constraints
│   └── res_company.py            # Company extension + config settings
├── views/
│   ├── report_theme_profile_views.xml    # CRUD views for theme profiles
│   └── res_config_settings_views.xml     # Settings screen integration
├── report/
│   ├── report_invoice_inherit.xml        # Invoice report override
│   ├── report_sale_order_inherit.xml     # Sale order report override
│   └── report_purchase_order_inherit.xml # Purchase order report override
├── security/
│   └── ir.model.access.csv
├── data/
│   └── default_theme_data.xml    # Ships a default theme on install
└── static/description/
    └── icon.png
```

---

## Notes

- One default theme is enforced per company via a Python constraint
- Watermark opacity is validated between 0.05 and 0.5
- Font sizes are validated (body: 6–20pt, heading: 8–30pt)
- The default theme installs automatically and can be customized freely
- RTL layout flips text direction and switches to the selected Arabic font

---

## Author

**Umar Ahmad Rafi**
Odoo Developer | umarahmadrafi@gmail.com
[LinkedIn](https://www.linkedin.com/in/umar-ahmad-rafi) · [GitHub](https://github.com/umarahmadrafi008)

---

## License

[LGPL-3](https://www.gnu.org/licenses/lgpl-3.0.en.html)