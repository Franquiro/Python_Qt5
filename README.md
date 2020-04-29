# Python_Qt5

[Guia de PyQt5](https://www.zetcode.com/gui/pyqt5)
* GUI.py - Primer intento de interfaz grafica en python con Qt

## PyQt_1 - Date & Time
Requires import from QtCore
PyQt5 has QDate, QDateTime, QTime classes
* QDate: class for working with calendar date in the Gregorian Calendar.
    * Methods for determining the date, comparing or manipulating dates
* QTime: class for working with clock time.
    * Methods for comparing time, determining time and various for manipulating time.
* QDateTime: combines QDate and QTime into one class

### Current date and time
**PyQt5 has:**
* currentDate()
* currentTime()
* currentDateTime()


* Date and time formats:
    * Qt.ISODate
    * Qt.DefaultLocaleLongDate
    * Qt.DefaultLocaleShortDate
* Methods on date objects
    * __datevariable.toUTC():__ returns the date in UTC time.
    * __datevariable.offsetFromUtc():__ returns the difference between _Local_ and _UTC_ time in seconds.
    * __datevariable.daysInMonth():__ returns the days in the month.
    * __datevariable.daysInYear():__ returns the days in a year.
    * __datevariable.daysTo(datevariable2):__ returns the difference in days between _datevariable_ and _datevariable2_
### Datetime Arithmetics
Datetime variables have methods that allow us to do arithmetic operations on them. Some methods include:
* __Adding Days:__ dateTimeVariable.addDays(n)
* __Substracting Days:__ dateTimeVariable.addDays(-n)
* __Adding Seconds:__ dateTimeVariable.addSecs(n)
* __Adding Months:__ dateTimeVariable.addMonths(n)
* __Adding Years:__ dateTimeVariable.addYears(n)