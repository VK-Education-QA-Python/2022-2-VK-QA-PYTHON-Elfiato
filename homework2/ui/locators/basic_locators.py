from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_BUTTON_IN_HEADER = (By.CSS_SELECTOR, "[class^='responseHead-module-button']")


class LoginPageLocators:
    EMAIL_FIELD = (By.CSS_SELECTOR, "[name=email]")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "[name=password]")
    LOGIN_BUTTON_IN_AUTHORIZATION_FORM = (By.CSS_SELECTOR, "[class^=authForm-module-button]")


class DashboardPageLocators:
    USER_NAME_BUTTON = (By.CSS_SELECTOR, "[class^=right-module-userNameWrap]")
    CREATE_CAMPAIGN_BUTTON = (By.CSS_SELECTOR,
                              "[class*='dashboard-module-createButtonWrap'] [class*='button-module-button']")
    CREATED_CAMPAIGNS = (By.CSS_SELECTOR, "a[class*='campaignNameLink']")


class CreatingCampaignPageLocators:
    TRAFFIC = (By.CSS_SELECTOR, "._traffic")
    URL_FIELD = (By.CSS_SELECTOR, ".js-main-url-wrap input")
    CAMPAIGN_NAME = (By.CSS_SELECTOR, ".base-settings__campaign-name-wrap input")
    SOCIAL_CHARACTERISTICS = (By.CSS_SELECTOR, "li[data-name='interests_soc_dem'] .setting-header__normal-wrapper")
    EDUCATION_LIST = (By.CSS_SELECTOR,
                      "li[data-name='interests_soc_dem'] .fast-tree-item:nth-child(5) .fast-tree-item__collapse-icon")
    HIGHER_EDUCATION = (By.CSS_SELECTOR,
                        "li[data-name='interests_soc_dem'] .fast-tree-item:nth-child(5) "
                        "ul .fast-tree-item:nth-child(1) input")
    INTERESTS = (By.CSS_SELECTOR, "li[data-name='interests'] .setting-header")
    MUSIC = (By.CSS_SELECTOR,
             "li[data-name='interests'] .fast-tree-item:nth-child(20) .fast-tree-item__collapse-icon")
    ROCK = (By.CSS_SELECTOR,
            "li[data-name='interests'] .fast-tree-item:nth-child(20) ul .fast-tree-item:nth-child(6) input")
    AD_FORMAT_TEASER = (By.CSS_SELECTOR, "[id^='patterns_teaser']")
    SHOW_MEDIA_LIB_BUTTON = (By.CSS_SELECTOR, "[data-test='button-show-medialib']")
    UPLOAD_IMAGE_BUTTON = (By.CSS_SELECTOR, "[data-test='button-upload']")
    IMAGE_INPUT = (By.CSS_SELECTOR, "[class^='bannerForm-module-fieldsWrapForInline'] input")
    TEASER_LINK = (By.CSS_SELECTOR, "input[data-name='primary']")
    TEASER_TITLE = (By.CSS_SELECTOR, "input[data-name^='title']")
    TEASER_TEXT = (By.CSS_SELECTOR, "textarea[data-name^='text']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, ".footer__button .button_submit")


class SegmentsPageLocators:
    CREATE_SEGMENT_BUTTON = (By.CSS_SELECTOR, ".button_submit")
    CREATED_SEGMENTS = (By.CSS_SELECTOR, "[class^='main-module-CellFirst']")
    SUBMIT_REMOVE_BUTTON = (By.CSS_SELECTOR, ".button_confirm-remove")


class CreatingSegmentLocators:
    APPS_CATEGORY = (By.XPATH,
                     "//div[text()='Приложения и игры в соцсетях' or text()='Apps and games in social networks']")
    SEGMENT_CHECKBOX = (By.CSS_SELECTOR, ".adding-segments-source__checkbox")
    SUBMIT_SEGMENT_BUTTON = (By.CSS_SELECTOR, ".adding-segments-modal__btn-wrap .button_submit")
    CREATE_NEW_SEGMENT_BUTTON = (By.CSS_SELECTOR, ".create-segment-form__btn-wrap .button_submit")
    SEGMENT_NAME_FORM = (By.CSS_SELECTOR, ".input_create-segment-form  input")
    GROUPS_CATEGORY = (By.XPATH,
                       "//div[text()='Группы ОК и VK' or text()='Groups OK and VKs']")


class GroupListPageLocators:
    GROUP_LIST_IN_LEFT_MENU = (By.XPATH, "//span[text()='Группы ОК и VK' or text()='Groups OK and VK']")
    GROUP_URL_INPUT_FIELD = (By.CSS_SELECTOR, ".segments-groups-ok-list__add-theme input")
    SELECT_ALL = (By.CSS_SELECTOR, "[data-test='select_all']")
    ADD_SELECTED_ITEMS_BUTTON = (By.CSS_SELECTOR, "[data-test='add_selected_items_button']")
    ALL_ADDED_GROUPS = (By.CSS_SELECTOR, ".flexi-table__row")
    SUBMIT_REMOVE_BUTTON = (By.CSS_SELECTOR, ".button_confirm-remove")
