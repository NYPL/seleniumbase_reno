from seleniumbase import BaseCase


class BlogAllPage(BaseCase):
    explore_by = '//*[@id="search-filters--heading"]'
    search_results = '//*[@id="search-results-details"]'

    clear_all_search_terms = '//*[@id="search-results-details__button"]'

    channels = '//*[@id="multiselect-channel"]/button'
    channel_links = '//*[@id="multiselect-channel"]/div/ul'
    clear_channel = '//*[@id="multiselect-button-clear-channel"]'
    apply_channel = '//*[@id="multiselect-button-save-channel"]'
    asian_american = '//*[contains(text(), "Asian American & Pacific Islander Culture")]'

    subjects = '//*[@id="multiselect-subject"]/button'
    apply_subject = '//*[@id="multiselect-button-save-subject"]'

    libraries = '//*[@id="multiselect-library"]/button'
    apply_library = '//*[@id="multiselect-button-save-library"]'
    clear_library = '//*[@id="multiselect-button-clear-library"]'

    divisions = '//*[@id="multiselect-division"]/button'
    apply_division = '//*[@id="multiselect-button-save-division"]'
    clear_division = '//*[@id="multiselect-button-clear-division"]'

    audience = '//*[@id="multiselect-audience_by_age"]/button'
    apply_audience = '//*[@id="multiselect-button-save-audience_by_age"]'
    clear_audience = '//*[@id="multiselect-button-clear-audience_by_age"]'

    adults = '//*[@id="multiselect-audience_by_age"]//li[1]//label'
    kids = '//*[@id="multiselect-audience_by_age"]//li[2]//label'
    teens = '//*[@id="multiselect-audience_by_age"]//li[3]//label'

    li_dic = {"asian_american": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[1]/div/label/span[2]'
        , "biography": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[2]/div/label/span[2]',
              "black_culture": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[3]/div/label/span[2]',
              "book_lists": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[4]/div/label/span[2]',
              "comics_graphic": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[5]/div/label/span[2]',
              "digital_collections": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[6]/div/label/span[2]',
              "doc_chat": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[7]/div/label/span[2]',
              "early_literacy": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[8]/div/label/span[2]',
              "espanol_spanish": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[9]/div/label/span[2]',
              "for_kids": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[10]/div/label/span[2]',
              "for_teachers": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[11]/div/label/span[2]',
              "for_teens": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[12]/div/label/span[2]',
              "francais_french": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[13]/div/label/span[2]',
              "hispanic_latinx": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[14]/div/label/span[2]',
              "horror": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[15]/div/label/span[2]',
              "lgbtq+": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[16]/div/label/span[2]',
              # "library_stories": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[17]/div/label/span[2]',
              "library_talks": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[17]/div/label/span[2]',
              "mysteries_crime": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[18]/div/label/span[2]',
              "nonfiction": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[19]/div/label/span[2]',
              "poetry": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[20]/div/label/span[2]',
              "popular_culture": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[21]/div/label/span[2]',
              "research_at_nypl": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[22]/div/label/span[2]',
              "romance": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[23]/div/label/span[2]',
              "science_fiction": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[24]/div/label/span[2]',
              "the_librarian": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[25]/div/label/span[2]',
              "women's_history": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[26]/div/label/span[2]',
              "work_cited": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[27]/div/label/span[2]',
              "chinese_language": '/html/body/div[1]/div/div[2]/main/div[1]/div[2]/div/div/div/div/div[1]/div/ul/li[28]/div/label/span[2]',

              "art": '//*[@id="multiselect-subject"]/div/ul/li[1]/div/label/span[2]',
              "business": '//*[@id="multiselect-subject"]/div/ul/li[2]/label/span[2]',
              "genealogy": '//*[@id="multiselect-subject"]/div/ul/li[3]/label/span[2]',
              "history": '//*[@id="multiselect-subject"]/div/ul/li[4]/label/span[2]',
              "nyc_history": '//*[@id="multiselect-subject"]/div/ul/li[5]/label/span[2]',
              "performing_arts": '//*[@id="multiselect-subject"]/div/ul/li[6]/label/span[2]',
              "science": '//*[@id="multiselect-subject"]/div/ul/li[7]/label/span[2]'
              }

    location_dic = {'Art & Architecture Collection': 'Stephen A. Schwarzman Building',
                    'Art and Artifacts Division': 'Schomburg Center for Research in Black Culture',
                    'Billy Rose Theatre Division': 'The New York Public Library for the Performing Arts',
                    'Carl H. Pforzheimer Collection of Shelley and His Circle': 'Stephen A. Schwarzman Building',
                    'DeWitt Wallace Periodical Room': 'Stephen A. Schwarzman Building',
                    'Dorot Jewish Division': 'Stephen A. Schwarzman Building',
                    'General Research Division': 'Stephen A. Schwarzman Building',
                    'George Arents Collection': 'Stephen A. Schwarzman Building',
                    'Henry W. and Albert A. Berg Collection of English and American Literature': 'Stephen A. Schwarzman Building',
                    'Irma and Paul Milstein Division of United States History, Local History and Genealogy': 'Stephen A. Schwarzman Building',
                    'Jean Blackwell Hutson Research and Reference Division': 'Schomburg Center for Research in Black Culture',
                    'Jerome Robbins Dance Division': 'The New York Public Library for the Performing Arts',
                    'Lionel Pincus and Princess Firyal Map Division': 'Stephen A. Schwarzman Building',
                    'Manuscripts and Archives Division': 'Stephen A. Schwarzman Building',
                    'Manuscripts, Archives and Rare Books Division': 'Schomburg Center for Research in Black Culture',
                    'Moving Image and Recorded Sound Division': 'Schomburg Center for Research in Black Culture',
                    'Music Division': 'The New York Public Library for the Performing Arts',
                    'Photographs and Prints Division': 'Schomburg Center for Research in Black Culture',
                    'Photography Collection': 'Stephen A. Schwarzman Building',
                    'Picture Collection': 'Stephen A. Schwarzman Building',
                    'Print Collection': 'Stephen A. Schwarzman Building',
                    'Rare Book Division': 'Stephen A. Schwarzman Building',
                    'Spencer Collection': 'Stephen A. Schwarzman Building',
                    'The Rodgers and Hammerstein Archives of Recorded Sound': 'The New York Public Library for the Performing Arts',
                    'Theatre on Film and Tape Archive': 'The New York Public Library for the Performing Arts'}

    def open_blog_page_all(self):
        # self.open("https://www.nypl.org/blog/all")

        if self.env == "qa":
            print("Running on QA Env")
            self.open("https://qa-www.nypl.org/blog/all")

        else:
            print("Running on Production Env")
            self.open("https://www.nypl.org/blog/all")

