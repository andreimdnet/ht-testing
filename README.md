# Home Task - testing project

Python project built with the latest versions of:
- selenium 
- webdriver-manager 
- pytest 

Structure:
- "base_page.py" contains utility/common methods 
to be used across various page objects;
- 3 classes/page objects for Twitch main page, Twitch results 
page and Twitch streamer page; each page has its own locator 
and wrappers over the common methods from base;
- "conftest.py" contains a 'pytest' fixture used for 
initialising (via webdriver-manager) the driver object with
parameterized mobile emulation, url launching and driver object
disposing;
- "base_test.py" marked as using the fixture from above
and used inside the test, enabling access to the driver object
which subsequently is used by all page objects constructors;
- "test_data.py" contains the url and 2 mobile devices types;

