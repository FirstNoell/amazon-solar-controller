Web Scraping Project Summary
Project Title: Amazon Solar Charge Controller Data Crawler
Client: [Jimmy A Javier]
Developer: Leoncio U. Coronado Jr.
Date: July 4, 2025
________________________________________
 Project Objectives
•	Automate the extraction of product listings for solar charge controllers from Amazon.com
•	Extract the following data:
o	Product Title
o	Product URL
o	Current Price
o	Original List Price
•	Enable automatic navigation through pagination
•	Bypass Amazon's bot detection for uninterrupted scraping
________________________________________
Technologies Used
Component	Tool
Scraping Engine	Scrapy 2.13.2
Browser Automation	Scrapy-Selenium (with ChromeDriver)
Bot Evasion	Custom User-Agent Rotation
Language	Python 3.9
Output Format	JSON
________________________________________
 Anti-Bot Strategy
•	Headless Selenium browser simulates real user interaction
•	Custom middleware rotates User-Agent headers with each request
•	Optional upgrade: proxy rotation for further anonymity
________________________________________
Pagination Support
•	Automatically identifies and follows the "Next" page link
•	Enables full product listing extraction across multiple pages
•	Resilient to layout changes
________________________________________
Sample Extracted Data
{
  "title": "Renogy 10 Amp 12V/24V PWM Negative Ground Solar Charge Controller",
  "product_link": "https://www.amazon.com/dp/B07NPDWZJ7",
  "price": "$16.99",
  "list_price": "$26.99"
}
________________________________________
Deliverables
•	 Fully functional Scrapy project folder
•	 Custom middleware for User-Agent rotation
 Output file: controller_pagination.json
•	 Ready for export to CSV, Excel, or database
________________________________________ Future Upgrades
•	Export to Excel/SQL
•	Proxy integration
•	Price change monitoring
•	Email or Slack alerts
•	Deployment on cloud scheduler (e.g., cron job)
________________________________________
 Contact Info
Developer: Leoncio U. Coronado Jr.
Email: coronadonoell@gmail.com
