# info
import requests
from bs4 import BeautifulSoup

def scraping():
    """
    Web scraping code
    """

    url = "https://www.bbc.com/sport/football/scores-fixtures/" + "2022-02-26"
    # url = "https://www.bbc.co.uk/sport/football/premier-league/scores-fixtures" + "2022-02"
    url = "https://www.premierleague.com/news/1754980"
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "html.parser")

    tags = ["span", "h3"]
    classes = (["gs-u-display-none gs-u-display-block@m qa-full-team-name sp-c-fixture__team-name-trunc",
                "sp-c-fixture__status-wrapper qa-sp-fixture-status",
                'sp-c-fixture__number sp-c-fixture__number--time', "sp-c-fixture__number sp-c-fixture__number--home",
                "sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--ft",
                "sp-c-fixture__number sp-c-fixture__number--home sp-c-fixture__number--live-sport",
                "sp-c-fixture__number sp-c-fixture__number--away sp-c-fixture__number--live-sport",
                "sp-c-fixture__number sp-c-fixture__number--away sp-c-fixture__number--ft",
                'gel-minion sp-c-match-list-heading'])

    scraper = soup.find_all(tags, attrs={'class': classes})
    data = [str(l) for l in scraper]

    print(data)


    return data


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = scraping()


