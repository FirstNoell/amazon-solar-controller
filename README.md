---

# Web Scraping Project Summary

**Project Title:** Amazon Solar Charge Controller Data Crawler  
**Client:** [Insert Client Name]  
**Developer:** [Your Name]  
**Date:** July 3, 2025

---

## Project Objectives

- Automate the extraction of product listings for solar charge controllers from Amazon.com  
- Extract the following data:
  - Product Title
  - Product URL
  - Current Price
  - Original List Price  
- Enable automatic navigation through pagination  
- Bypass Amazon's bot detection for uninterrupted scraping

---

## Technologies Used

| Component            | Tool                                 |
|----------------------|--------------------------------------|
| Scraping Engine      | Scrapy 2.13.2                        |
| Browser Automation   | Scrapy-Selenium (with ChromeDriver) |
| Bot Evasion          | Custom User-Agent Rotation          |
| Language             | Python 3.9                          |
| Output Format        | JSON                                 |

---

##  Anti-Bot Strategy

-  Headless Selenium browser simulates real user interaction  
-  Custom middleware rotates User-Agent headers with each request  
-  Optional upgrade: proxy rotation for further anonymity

---

##  Pagination Support

- Automatically identifies and follows the "Next" page link  
- Enables full product listing extraction across multiple pages  
- Resilient to layout changes

---

##  Sample Extracted Data

```json
{
  "title": "Renogy 10 Amp 12V/24V PWM Negative Ground Solar Charge Controller",
  "product_link": "https://www.amazon.com/dp/B07NPDWZJ7",
  "price": "$16.99",
  "list_price": "$26.99"
}
