# Sales Data Dashboard
# Individual Requirements 1 & 3
# Name: Grace Kulhanek

import pandas as pd
import numpy as np
import pyarrow
import time

storedResults = {}  # Stores completed analytics results for later


def loadCsv(filePath):
    print(f"Loading data from {filePath}...")
    startTime = time.time()

    requiredColumns = [
        "order_number",
        "employee_id",
        "employee_name",
        "job_title",
        "sales_region",
        "order_date",
        "order_type",
        "customer_type",
        "customer_name",
        "customer_state",
        "product_category",
        "product_number",
        "produce_name",
        "quantity",
        "unit_price"
    ]

    try:
        # Read the CSV and skip bad lines 
        df = pd.read_csv(filePath, engine="python", on_bad_lines="skip")
        assert isinstance(df, pd.DataFrame), "Loaded object is not a DataFrame."

        endTime = time.time()
        loadTime = endTime - startTime

        print(f"CSV file loaded successfully in {loadTime:.2f} seconds.")
        print(f"Number of rows: {len(df)}")
        print(f"Number of columns: {len(df.columns.tolist())}")
        print("Available columns:")
        print(df.columns.tolist())

        # Fill missing values
        df.fillna(0, inplace=True)

        # Convert important columns into useful types
        if "order_date" in df.columns:
            df["order_date"] = pd.to_datetime(
                df["order_date"],
                format="%m/%d/%Y",
                errors="coerce"
            )

        if "quantity" in df.columns:
            df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0)

        if "unit_price" in df.columns:
            df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce").fillna(0)

        # Create sales column for the pivot table 
        if "quantity" in df.columns and "unit_price" in df.columns:
            df["sales"] = df["quantity"] * df["unit_price"]
            df["sales"] = pd.to_numeric(df["sales"], errors="coerce").fillna(0)

        missingColumns = [col for col in requiredColumns if col not in df.columns]

        if missingColumns:
            print("Warning: Missing columns in the CSV file:")
            print(", ".join(missingColumns))
            print("Some analytics may not work.")
        else:
            print("All required columns are present.")

        return df

    except Exception as e:
        print(f"Error loading CSV file: {e}")
        print("Program ended because the file could not be loaded.")
        raise SystemExit


def chooseDataSource():
    # Lets the user choose which sales file to load
    defaultUrl = "https://drive.google.com/uc?id=1Fv_vhoN4sTrUaozFPfzr0NCyHJLIeXEA"
    alternateUrl = "sales_data.csv"

    print("Select sales data to load:")
    print("1. Default Google Drive sales data")
    print("2. Alternate local sales_data.csv file")
    print("3. Enter a custom file path or URL")

    userInput = input("Your choice: ").strip()

    if userInput == "1":
        return defaultUrl
    elif userInput == "2":
        return alternateUrl
    elif userInput == "3":
        customPath = input("Enter the file path or URL: ").strip()
        if customPath == "":
            print("No path entered. Using default Google Drive sales data.")
            return defaultUrl
        return customPath
    else:
        print("Invalid choice. Using default Google Drive sales data.")
        return defaultUrl


def checkRequiredColumns(dataFrame, requiredColumns):

    # Used so missing columns do not crash the program
    assert isinstance(requiredColumns, list), "requiredColumns must be a list."
    missingColumns = [col for col in requiredColumns if col not in dataFrame.columns]

    if missingColumns:
        print("Required columns for this analysis are missing:")
        print(", ".join(missingColumns))
        return False
    return True


def saveResult(resultName, resultData):
    # Store a copy so the user can view/export past results later
    storedResults[resultName] = resultData.copy()


def askToExport(resultData, defaultFileName):
    # Ask after each result if it should be exported to Excel
    exportChoice = input("Do you want to export these results to an Excel file? (y/n): ").strip().lower()

    if exportChoice != "y":
        return

    fileName = input(f"Enter Excel filename (default: {defaultFileName}.xlsx): ").strip()

    if fileName == "":
        fileName = f"{defaultFileName}.xlsx"
    elif not fileName.endswith(".xlsx"):
        fileName = f"{fileName}.xlsx"

    try:
        resultData.to_excel(fileName)
        print(f"Results exported to {fileName}")
    except Exception as e:
        print(f"Could not export results: {e}")


def showAndHandleResult(resultName, resultData, defaultFileName):
    print(resultName + ":")
    print(resultData)
    saveResult(resultName, resultData)
    askToExport(resultData, defaultFileName)


def displayInitialRows(dataFrame):
    # Preview first n rows, all rows, or skip
    totalRows = len(dataFrame)

    print("Enter rows to display:")
    print(f"- Enter a number 1 to {totalRows}")
    print("- To see all rows, enter 'all'")
    print("- To skip preview, press Enter")

    userInput = input("Your choice: ").strip().lower()

    if userInput == "":
        print("Skipping preview.")
        return
    elif userInput == "all":
        previewData = dataFrame.copy()
        showAndHandleResult("All sales data rows", previewData, "all_sales_rows")
    elif userInput.isdigit():
        rowCount = int(userInput)
        if 1 <= rowCount <= totalRows:
            previewData = dataFrame.head(rowCount).copy()
            showAndHandleResult(f"First {rowCount} rows of sales data", previewData, f"first_{rowCount}_rows")
        else:
            print("Invalid number of rows.")
    else:
        print("Invalid input. Please try again.")


def totalSalesByRegionAndOrderType(dataFrame):
    # Pivot table: total sales by region with order type as column groups
    requiredColumns = ["sales_region", "order_type", "sales"]
    if not checkRequiredColumns(dataFrame, requiredColumns):
        return

    pivotTable = pd.pivot_table(
        dataFrame,
        index="sales_region",
        columns="order_type",
        values="sales",
        aggfunc="sum",
        margins=True,
        margins_name="Total"
    )

    showAndHandleResult(
        "Total sales by region and order_type",
        pivotTable,
        "total_sales_by_region_and_order_type"
    )


def averageSalesByRegionStateAndSaleType(dataFrame):
    # Pivot table: average sales by region with customer state and order type as column groups
    requiredColumns = ["sales_region", "customer_state", "order_type", "sales"]
    if not checkRequiredColumns(dataFrame, requiredColumns):
        return

    pivotTable = pd.pivot_table(
        dataFrame,
        index="sales_region",
        columns=["customer_state", "order_type"],
        values="sales",
        aggfunc="mean",
        margins=True,
        margins_name="Average"
    )

    showAndHandleResult(
        "Average sales by region with average sales by state and sale type",
        pivotTable,
        "average_sales_by_region_state_sale_type"
    )


def salesByCustomerTypeAndOrderTypeByState(dataFrame):
    # Pivot table: sales by customer type and order type, grouped by state
    requiredColumns = ["customer_type", "order_type", "customer_state", "sales"]
    if not checkRequiredColumns(dataFrame, requiredColumns):
        return

    pivotTable = pd.pivot_table(
        dataFrame,
        index=["customer_state", "customer_type"],
        columns="order_type",
        values="sales",
        aggfunc="sum",
        margins=True,
        margins_name="Total"
    )

    showAndHandleResult(
        "Sales by customer type and order type by state",
        pivotTable,
        "sales_by_customer_type_order_type_state"
    )


def totalSalesQuantityAndPriceByRegionAndProduct(dataFrame):
    # Pivot table: total quantity and sales by region and product
    requiredColumns = ["sales_region", "produce_name", "quantity", "sales"]
    if not checkRequiredColumns(dataFrame, requiredColumns):
        return

    pivotTable = pd.pivot_table(
        dataFrame,
        index=["sales_region", "produce_name"],
        values=["quantity", "sales"],
        aggfunc="sum",
        margins=True,
        margins_name="Total"
    )

    showAndHandleResult(
        "Total sales quantity and price by region and product",
        pivotTable,
        "total_sales_quantity_price_region_product"
    )


def totalSalesQuantityAndPriceByCustomerType(dataFrame):
    # Pivot table: total quantity and sales by order type and customer type
    requiredColumns = ["order_type", "customer_type", "quantity", "sales"]
    if not checkRequiredColumns(dataFrame, requiredColumns):
        return

    pivotTable = pd.pivot_table(
        dataFrame,
        index=["order_type", "customer_type"],
        values=["quantity", "sales"],
        aggfunc="sum",
        margins=True,
        margins_name="Total"
    )

    showAndHandleResult(
        "Total sales quantity and price by order and customer type",
        pivotTable,
        "total_sales_quantity_price_order_customer_type"
    )


def maxAndMinSalesPriceByCategory(dataFrame):
    # Pivot table: max and min sales by product category
    requiredColumns = ["product_category", "sales"]
    if not checkRequiredColumns(dataFrame, requiredColumns):
        return

    cleanDataFrame = dataFrame[["product_category", "sales"]].copy()
    cleanDataFrame["sales"] = pd.to_numeric(cleanDataFrame["sales"], errors="coerce").fillna(0)

    pivotTable = pd.pivot_table(
        cleanDataFrame,
        index="product_category",
        values="sales",
        aggfunc=["max", "min"],
        margins=True,
        margins_name="Overall"
    )

    showAndHandleResult(
        "Max and min sales price of sales by category",
        pivotTable,
        "max_min_sales_by_category"
    )


def showEmployeesByRegion(dataFrame):
    # Count unique employees by region using a pivot table
    requiredColumns = ["sales_region", "employee_id"]
    if not checkRequiredColumns(dataFrame, requiredColumns):
        return

    # Drop duplicates first so the same employee is not counted twice in one region
    uniqueEmployees = dataFrame.drop_duplicates(subset=["sales_region", "employee_id"])

    pivotTable = pd.pivot_table(
        uniqueEmployees,
        index="sales_region",
        values="employee_id",
        aggfunc="count",
        margins=True,
        margins_name="Total"
    )

    showAndHandleResult(
        "Number of unique employees by region",
        pivotTable,
        "unique_employees_by_region"
    )


def parseNumberChoices(userInput, maxChoice, allowEmpty=False):
    # Creates number choices like 1,2,3 into list indexes and seperated by commas
    assert isinstance(maxChoice, int) and maxChoice > 0, "maxChoice must be a positive integer."

    if allowEmpty and userInput.strip() == "":
        return []

    if userInput.strip() == "":
        return None

    splitValues = userInput.split(",")
    selectedIndexes = []

    for value in splitValues:
        cleanValue = value.strip()

        if not cleanValue.isdigit():
            return None

        numberValue = int(cleanValue)
        if numberValue < 1 or numberValue > maxChoice:
            return None

        zeroBasedIndex = numberValue - 1
        if zeroBasedIndex not in selectedIndexes:
            selectedIndexes.append(zeroBasedIndex)

    return selectedIndexes


def chooseFields(fieldList, promptText, allowEmpty=False):
    # Displays numbered choices and returns the selected field names
    assert isinstance(fieldList, list) and len(fieldList) > 0, "fieldList must be a non-empty list."

    print(promptText)
    for i, fieldName in enumerate(fieldList, start=1):
        print(f"{i}. {fieldName}")

    if allowEmpty:
        userInput = input("Enter the number(s) of your choice(s), separated by commas (enter for no grouping): ").strip()
    else:
        userInput = input("Enter the number(s) of your choice(s), separated by commas: ").strip()

    selectedIndexes = parseNumberChoices(userInput, len(fieldList), allowEmpty=allowEmpty)

    if selectedIndexes is None:
        print("Invalid selection.")
        return None

    selectedFields = [fieldList[index] for index in selectedIndexes]
    return selectedFields


def createCustomPivotTable(dataFrame):
    # Interactive custom pivot table builder that lets the user choose rows, columns, values, and aggregation function
    rowOptions = ["employee_name", "sales_region", "product_category"]
    columnOptions = ["order_type", "customer_type"]
    valueOptions = ["quantity", "sales"]
    aggOptions = ["sum", "mean", "count"]

    rowsSelected = chooseFields(rowOptions, "Select rows:")
    if rowsSelected is None or len(rowsSelected) == 0:
        print("At least one row field is required.")
        return

    columnsSelected = chooseFields(columnOptions, "Select columns (optional):", allowEmpty=True)
    if columnsSelected is None:
        return

    valuesSelected = chooseFields(valueOptions, "Select values:")
    if valuesSelected is None or len(valuesSelected) == 0:
        print("At least one value field is required.")
        return

    print("Select aggregation function:")
    for i, aggName in enumerate(aggOptions, start=1):
        print(f"{i}. {aggName}")

    aggInput = input("Enter the number of your choice: ").strip()
    aggIndexes = parseNumberChoices(aggInput, len(aggOptions))

    if aggIndexes is None or len(aggIndexes) != 1:
        print("Invalid aggregation choice.")
        return

    aggChoice = aggOptions[aggIndexes[0]]
    customDataFrame = dataFrame.copy()

    # For sum/mean, make sure selected values are numeric first because bad data could cause the pivot table to fail. Count can work with any data type so it does not need this step.
    if aggChoice != "count":
        for valueField in valuesSelected:
            customDataFrame[valueField] = pd.to_numeric(
                customDataFrame[valueField],
                errors="coerce"
            ).fillna(0)

    if len(columnsSelected) == 0:
        pivotTable = pd.pivot_table(
            customDataFrame,
            index=rowsSelected,
            values=valuesSelected,
            aggfunc=aggChoice,
            margins=True,
            margins_name="Total"
        )
    else:
        pivotTable = pd.pivot_table(
            customDataFrame,
            index=rowsSelected,
            columns=columnsSelected,
            values=valuesSelected,
            aggfunc=aggChoice,
            margins=True,
            margins_name="Total"
        )

    pivotTable = pivotTable.infer_objects(copy=False)

    # Let the user name the stored custom pivot table
    customName = input("Enter a name to store this custom pivot table: ").strip()
    if customName == "":
        customName = f"Custom pivot table {len(storedResults) + 1}"

    showAndHandleResult(customName, pivotTable, customName.replace(" ", "_").lower())


def showStoredResults(_):
    # Lets the user redisplay any stored result from earlier menu actions
    if len(storedResults) == 0:
        print("No stored results yet.")
        return

    print("\n--- Stored Results ---")
    for i, resultName in enumerate(storedResults.keys(), start=1):
        print(f"{i}. {resultName}")

    viewChoice = input("Enter a result number to display it, or press Enter to return: ").strip()

    if viewChoice == "":
        return

    if not viewChoice.isdigit():
        print("Invalid selection.")
        return

    resultNumber = int(viewChoice)
    resultNames = list(storedResults.keys())

    if 1 <= resultNumber <= len(resultNames):
        selectedName = resultNames[resultNumber - 1]
        print(selectedName + ":")
        print(storedResults[selectedName])
        askToExport(storedResults[selectedName], selectedName.replace(" ", "_").lower())
    else:
        print("Invalid selection.")


def showStoredResultsSummary():
    # Shows completed analytics above the menu
    print("\nCompleted analytics stored:")
    if len(storedResults) == 0:
        print("- None yet")
    else:
        for resultName in storedResults.keys():
            print(f"- {resultName}")


def exitProgram(_):
    print("Exiting the program. Goodbye!")
    raise SystemExit


def showTestCases(_):
    # Built-in test case list for assignment documentation
    print("\n--- Test Cases ---")
    print("1. Load valid CSV URL and confirm row count, columns, and load time display.")
    print("2. Load invalid URL and confirm program exits with an error message.")
    print("3. Select alternate local file and confirm it loads.")
    print("4. Use preview with Enter and confirm no rows display.")
    print("5. Use preview with 'all' and confirm all rows display.")
    print("6. Use preview with a valid number like 5 and confirm first 5 rows display.")
    print("7. Use preview with invalid input like -1, 0, or text and confirm validation message.")
    print("8. Run each predefined pivot table option and confirm output appears.")
    print("9. Export a result to Excel and confirm file is created.")
    print("10. Choose not to export and confirm program continues normally.")
    print("11. Test menu choice with invalid number and confirm validation message.")
    print("12. Test custom pivot table with valid row, column, value, and aggregation choices.")
    print("13. Test custom pivot table with invalid field numbers and confirm validation message.")
    print("14. Test custom pivot table with Enter for optional columns and confirm it still works.")
    print("15. Confirm unique employee count does not double count duplicates within a region.")
    print("16. Confirm missing or bad numeric data is coerced and does not crash the program.")
    print("17. Confirm bad CSV lines are skipped and program still loads.")
    print("18. Confirm missing required columns produce warnings instead of crashes.")
    print("19. Confirm stored results appear above the menu after analytics are run.")
    print("20. Confirm stored results menu can redisplay and export saved results.")


def displayMenu(dataFrame):
    # Tuple menu makes it easy to add, remove, or reorder menu items
    menuOptions = (
        ("Show the first n rows of sales data", displayInitialRows),
        ("Total sales by region and order_type", totalSalesByRegionAndOrderType),
        ("Average sales by region with average sales by state and sale type", averageSalesByRegionStateAndSaleType),
        ("Sales by customer type and order type by state", salesByCustomerTypeAndOrderTypeByState),
        ("Total sales quantity and price by region and product", totalSalesQuantityAndPriceByRegionAndProduct),
        ("Total sales quantity and price customer type", totalSalesQuantityAndPriceByCustomerType),
        ("Max and min sales price of sales by category", maxAndMinSalesPriceByCategory),
        ("Number of unique employees by region", showEmployeesByRegion),
        ("Create a custom pivot table", createCustomPivotTable),
        ("Display all stored results", showStoredResults),
        ("Show test cases", showTestCases),
        ("Exit", exitProgram)
    )

    showStoredResultsSummary()

    print("\n--- Sales Data Dashboard ---")
    for i, option in enumerate(menuOptions, start=1):
        print(f"{i}. {option[0]}")

    userInput = input(f"Enter an option (1-{len(menuOptions)}): ").strip()

    if not userInput.isdigit():
        print("Invalid input. Please enter a number corresponding to the menu options.")
        return

    choice = int(userInput)

    if 1 <= choice <= len(menuOptions):
        action = menuOptions[choice - 1][1]
        action(dataFrame)
    else:
        print("Invalid choice. Please enter a number corresponding to the menu options.")


def main():
    # Main program flow: choose dataset, load it, then keep showing the menu
    pd.set_option("display.max_columns", None)  # Helps wide pivot tables display fully

    selectedPath = chooseDataSource()
    salesData = loadCsv(selectedPath)

    assert salesData is not None, "salesData should not be None after successful load."

    while True:
        print("\nSales Data Dashboard")
        displayMenu(salesData)


if __name__ == "__main__":
    main()