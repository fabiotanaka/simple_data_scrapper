import requests
from requests import RequestException
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


def get_html(url):
    try:
        uClient = uReq(url)
        page_html = uClient.read()
        uClient.close()
        return page_html
    except RequestException as e:
        print('error')


if __name__ == '__main__':
    url = 'http://allrecipes.com.br/receita/2454/bolo-de-cenoura-de-liquidificador.aspx'
    page_soup = soup(get_html(url), 'html.parser')

    # recipe title
    recipe_title = page_soup.h1.span.text.strip()
    print(recipe_title)
    # review count
    review_count = page_soup.findAll('span', {'class': 'review-count'})[0].text[1:-1]
    print(review_count)
    # star_count
    star_count = len(page_soup.findAll('span', {'class': 'icon-star'})) + \
                 len(page_soup.findAll('span', {'class': 'icon-star-half'}))*0.5
    print(star_count)
    # description
    recipe_description = page_soup.findAll('p', {'class': 'description'})[0].text.strip()
    print(recipe_description)
    # recipe_owner
    recipe_owner = page_soup.findAll('div', {'class': 'profile-name-wrapper'})[0].a.text.strip()
    print(recipe_owner)
    # people_done
    people_done = page_soup.findAll('div', {'class': 'imiContainer'})[0].span.text.strip()
    print(people_done)
    # n_servings
    n_servings = page_soup.findAll('span', {'class': 'accent'})[0].text.replace('\xa0','')
    print(n_servings)
    # ingredients
    ingredients = ''
    ingredients_section = page_soup.findAll('section', {'class': 'recipeIngredients gridResponsive__module'})[0]
    for ingredient in ingredients_section.findAll('li'):
        ingredients = ingredients + ' ' + ingredient.span.text
    print(ingredients)


