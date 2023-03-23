                                              **Python selenium in BrowserStack- with POM pattern**

The project is created in Python and selenium framework and it is intergrated to BrowserStack. 
It is a sample skeleton using the defined framework.

Automation for https://www.amazon.com/ website.

Scenarios covered:
1. Open Amazon page and check whether the page loads 
2. Search for an item 

**Pre condition**

Intellij IDE with selenium
python
Edit/Add BrowserStack Access_key and User name in .env file

**Best Practices**

1. Uses Page object model
2. Use Reusable Request
3. Uses testcases , testdata and locators from seperate files which enables easy maintablity and reuse 

**How to Run**

1. Clone the repository 
2. Run 
 python -m unittest 
 
**How to check the result **

Check browserStack dashboard 
