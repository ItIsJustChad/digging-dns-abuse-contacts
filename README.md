# Registrar and Registry Abuse Contact Finder by Digging DNS

This project provides up-to-date, easy-to-use lists of abuse contact information for domain name registrars and registries, making it simpler for network administrators, security researchers, and the public to report malicious activity. It tracks whether the entities uses an email address, webform, both, or if the information was found.

Want to bookmark a resource for easy searching and access? [Use Digging DNS to search this data](https://app.diggingdns.com/abuse-contacts).

**tl;dr**: I took a grand tour of every registrar's and registry's website worldwide to find the abuse contacts and put them in one spot so you don't have to.

## About This Project

Registrars and registries are required to provide a contact for submitting reports about abusive domains. However, this information has become more difficult to track in the wake of the updated agreements ICANN and their parties hold. [You can read more about it here](https://www.diggingdns.com/modules/tools/diggingdns-abuse-contacts).

This project solves that problem by providing a community resource to collaborate and track where abuse should be reported.

## License

This project is licensed under the MIT License. This data is **free for all personal and commercial use**. If you are using this data in a commercial product, I encourage you to support the project's continued maintenance.

<a href="https://www.buymeacoffee.com/chadls" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-blue.png" alt="Buy Me A Coffee" style="height: 42px !important;width: 151px !important;" ></a>

## Methodology for Version 1.0

The data here is gathered and verified with a straightforward, repeatable process:

1.  **Source:** I started with the official lists of accredited organizations provided by ICANN for both [Registrars](https://www.icann.org/en/accredited-registrars) and [Registries](https://www.icann.org/en/registry-agreements).
2.  **Investigation:** For each entity, I visited the website they have provided to ICANN. I spent **approximately one minute** attempting to locate a dedicated abuse contact email or web form.
3.  **Verification:**
      * If a clear abuse contact is found, the details are recorded, the `found` column is set to `true`, and the `as_of` column is set to the date of verification.
      * If the information is unclear, the website is down, or a contact cannot be located within the time limit, the relevant columns are marked as `unable to locate` and the `found` column is set to `false`.

Per their agreements with ICANN, both [Registrars (Section 3.18)](https://www.icann.org/en/system/files/files/registrar-accreditation-agreement-21jan24-en.pdf) and [Registry Operators (Section 4)](https://itp.cdn.icann.org/en/files/registry-agreements/base-registry-agreement-21-01-2024-en.pdf), are contractually obligated to maintain and publish an abuse contact. For the updated abuse amendments, [ICANN published the following advisors](https://www.icann.org/en/contracted-parties/advisories/documents/advisory-compliance-with-dns-abuse-obligations-in-the-registrar-accreditation-agreement-and-the-registry-agreement-05-02-2024-en):
* **Registrars**: To facilitate submission of reports from any party alleging abuse and/or Illegal Activity, the registrar must publish an email address or web form that is readily accessible on the homepage of the registrar's website4. Web forms must not require a login to submit abuse reports. A registrar's homepage that clearly displays a link to a "Report Abuse'' or a "Contact Us" page (which clearly includes the abuse contact) and that allows reporters to easily submit reports from the linked page will be deemed compliant.
* **Registries**: To facilitate submission of reports from any party alleging malicious conduct in the TLD, including DNS Abuse, the registry operator must publish an email address or web form, a mailing address, and a primary contact for handling such reports. A registry operator's homepage that clearly displays a link to a "Report Abuse'' or a "Contact Us" page (which clearly includes the abuse contact) where submission of reports is unimpeded will be deemed compliant.


## Data Structure

This repository contains two primary data files:

  * `registrars.csv`: Abuse contact information for domain registrars.
  * `registries.csv`: Abuse contact information for gTLD registries.

The columns in these files are defined as follows:

| Column | Description |
| :--- | :--- |
| **iana_id** | (Registrars only) The unique ID assigned to the registrar by IANA. |
| **tld** | (Registries only) The top-level domain managed by the registry. |
| **name** | The entity tied to the IANA ID or TLD. |
| **email** | The specific email address for abuse reports. |
| **form** | A direct URL to a web form for submitting abuse reports. |
| **notes** | Any relevant context, such as if the contact is a general one or if a login is required. |
| **found** | A boolean (`true`/`false`) indicating if I successfully located a clear abuse contact. |
| **as\_of** | The date (YYYY-MM-DD) when the information was last verified. |


## Contributing

Contributions are welcome and greatly appreciated\! You can help keep this data accurate and up-to-date. Please follow these steps to contribute:

1.  **Fork** the repository.
2.  Create a new **branch** for your changes (e.g., `git checkout -b update-registrar-xyz`).
3.  Make your changes to the relevant `.csv` file.

#### Adding, Updating, or Removing Rows

  * **To Add a New Entry:** Add a new line to the end of the appropriate CSV file, filling in all columns according to the Data Structure table above. Set the `as_of` date to the current date.
  * **To Update an Existing Entry:** Find the row for the entity you are updating. Modify the columns with the new, correct information. **Crucially, update the `as_of` column to the current date** so I know when it was last verified.
  * **To Remove an Entry:** If a registrar has been de-accredited or a registry has been decommissioned, you can remove the entire row.

#### Syncing JSON and Submitting

1.  After editing a `.csv` file, please run the conversion script to ensure the JSON files are in sync with your changes:
    ```bash
    python convert_to_json.py
    ```
2.  **Commit** your changes with a clear and descriptive message (e.g., "Update abuse contact for Registrar XYZ").
3.  **Push** your branch to your forked repository.
4.  Open a **Pull Request** back to this main repository. I will review it as soon as possible\!