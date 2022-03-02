from src.Store.Cache import CACHE_STORE

def return_Data_From_Cache():
    data = CACHE_STORE.getCache()
    return data


# def return_Data_From_Database():
#     pass


# # @app.route("/", methods=["GET"])
# def check_cache_for_data():
#     pass


# # @app.route("/", methods=["POST",])
# def update_Library(request):
#     pass

# def persist_To_Database():
#     pass
