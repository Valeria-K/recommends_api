from aiohttp import web
from csv_search import find_recommendations_in_csv

CSV_FILE_PATH = 'recommends.csv'


def is_convertible_to_float(string):
    try:
        float(string)
        return True
    except:
        return False


async def get_recommendations(request: web.Request) -> web.Response:
    sku = request.query.get('sku')
    min_rank = float(request.query.get('min_rank')) if is_convertible_to_float(request.query.get('min_rank')) else 0

    if not sku:
        return web.json_response({'err': 'sku is required'})

    recommendations, err = find_recommendations_in_csv(CSV_FILE_PATH, sku, min_rank)
    response_obj = {'recommendations': recommendations, 'err': err}
    return web.json_response(response_obj)


app = web.Application()
app.router.add_get('/recommendations', get_recommendations)

web.run_app(app)
