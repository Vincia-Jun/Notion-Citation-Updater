# Notion Citation Updater
<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

The **Notion Citation Updater** is a Python script designed to automate the process of updating citation counts for academic papers stored in a Notion database. By leveraging the power of the Scholarly library, this tool searches for publications by title and retrieves their citation information.




<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/shaojintian/Best_README_template/">
    <img src="images/logo.png" alt="Logo" width="546" height="235">
  </a>
</p>

## 📖 Introduction
I use a **Notion database** (tempelate refer to [paper_notion](https://frosted-hacksaw-782.notion.site/81473a1176454a17916de88f22fe79bd?v=ec80ed4fd3b248efbb2c23a8055ef268)) as my literature management tool. However, it can't update citation counts for articles in real time. Therefore, I aim to use Python to implement real-time updates of citation counts.

The **Notion Citation Updater** is a Python script designed to automate the process of updating citation counts for academic papers stored in a **Notion database**. By leveraging the power of the Scholarly library, this tool searches for publications by title and retrieves their citation information. Notion Citation Updater requires configuration in two aspects:
- **Notion Integration:** obtain the API for the Notion database, used to add, delete, query, and modify the database.
- **scholarly:** a Python module for retrieving academic literature information from Google Scholar.

## 🤖 Notion Integration
**Notion integrations** using the API allow you to connect and interact with Notion’s features programmatically.

- **Step1:** Creat your own notion integration from [here](https://www.notion.so/profile/integrations).
- **Step2:** Copy the "Internal Integration Secret", which will be used in Python to access the database.
- **Step3:** Navigate to the database you want your integration to interact with. Connect this page to your previously created integration by clicking the "..." menu in the top-right corner of the page.

Hence, your integration now has access to your dataset/page. You can use Python to interact with this database, performing actions like updating existing entries or creating new pages.



<!-- links -->
[your-project-path]:Vincia-Jun/Notion-Citation-Updater
[contributors-shield]: https://img.shields.io/github/contributors/Vincia-Jun/Notion-Citation-Updater.svg?style=flat-square
[contributors-url]: https://github.com/Vincia-Jun/Notion-Citation-Updater/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Vincia-Jun/Notion-Citation-Updater.svg?style=flat-square
[forks-url]: https://github.com/Vincia-Jun/Notion-Citation-Updater/network/members
[stars-shield]: https://img.shields.io/github/stars/Vincia-Jun/Notion-Citation-Updater.svg?style=flat-square
[stars-url]: https://github.com/Vincia-Jun/Notion-Citation-Updater/stargazers
[issues-shield]: https://img.shields.io/github/issues/Vincia-Jun/Notion-Citation-Updater.svg?style=flat-square
[issues-url]: https://img.shields.io/github/issues/Vincia-Jun/Notion-Citation-Updater.svg
