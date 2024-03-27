def input_text_Xpath(driver, wait, data, Xpath):
    """
    :param driver: WebDriver instance
    :param wait: WebDriverWait instance
    :param data: data to be inputted
    :param Xpath: Xpath of the element to be inputted
    :return: None
    """
    try:
        element = wait.until(EC.presence_of_element_located((By.XPATH, Xpath)))
        element.clear()
        element.send_keys(data)
        print(f"Inputted '{data}' in the element with Xpath: {Xpath}")
    except Exception as e:
        print(f"Failed to input text in the element with Xpath: {Xpath}. Exception: {e}")
        raise e

