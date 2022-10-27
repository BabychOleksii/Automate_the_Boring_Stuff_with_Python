# import traceback
#
# # raise exception
#
# try:
#     raise Exception('This is the error message.')
# except:
#     errorFile = open('error_log.txt', 'a')
#     errorFile.write(traceback.format_exc())
#     errorFile.close()
#     print('The traceback info was written into error_log.txt')

# =============================================================

# assertion

market_2nd = {'ns': 'green', 'ew': 'red'}

def switchLight(intersection):
    for key in intersection.keys():
        if intersection[key] == 'green':
            intersection[key] = 'yellow'
        elif intersection[key] == 'yellow':
            intersection[key] = 'red'
        elif intersection[key] == 'red':
            intersection[key] = 'green'
    assert 'red' in intersection.values(), 'Neither light is red!' + str(intersection)

print(market_2nd)
switchLight(market_2nd)
print(market_2nd)