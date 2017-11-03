import json
import Params

def main():
    test_config = Params.params_1
    params = test_config['post_data']

    #print(params)

    #print(test_config['post_data']['data'])
    #print(json.dumps(test_config['post_data']['data'], sort_keys=False, separators=(',', ': ')))

    params.update({'data': json.dumps(test_config['post_data']['data'], sort_keys=False, separators=(',', ': '))})


    print(params)

main()