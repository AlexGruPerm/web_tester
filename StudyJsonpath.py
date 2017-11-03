import logging
import Params

#logging.basicConfig(level = logging.DEBUG)
logging.basicConfig(format = u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s', level = logging.DEBUG)

def main():
    '''
    CRITICAL
    ERROR
    WARNING
    INFO
    DEBUG
    '''
try:
    test_config = Params.param_4
    logging.info('Begin parse params')

    #Check that all necessary keys exists in dict
    try:
        check_keys = ('name','url','headers','cookies','post_data','test_suc_time','test_suc_size')
        for ck in check_keys:
            if not ck in test_config:
                raise KeyError('Key '+ck+' not found in test config params.')
            elif not test_config.get(ck):
                raise ValueError('Value for Key ' + ck + ' is empty or None.')
    except KeyError as ek:
        logging.critical(ek.args)
        raise KeyError(ek.args)
        # here return or exit from execution
    except ValueError as ev:
        logging.critical(ev.args)
        raise ValueError(ev.args)
        # here return or exit from execution
    else:
        logging.info('All keys found in test config params.')
        name = test_config['name']
        url  = test_config['url']
        headers = test_config['headers']
        cookies = test_config['cookies']
        post_data = test_config['post_data']
        test_suc_time = test_config['test_suc_time']
        test_suc_size = test_config['test_suc_size']
        logging.info('All values in params checked for not None,Null')
        logging.info('Test name ('+name+') url ('+url+')')

    #print(name)
    #print(url)
    #print(headers)
    #print(cookies)
    for cook_key in cookies.keys():
        print(cook_key,"   ",cookies.get(cook_key).get('value'),"  ",cookies.get(cook_key).get('domain')," > ",cookies.get(cook_key).get('path')) #'domain': 'path':
    #print(post_data)
    #print(test_suc_time)
    #print(test_suc_size)

#check that value by founded key not empty

    # Separated parts of config param.
        #'name','url','headers','cookies'
except Exception as e:
    logging.critical('External exception handler: '+str(e.args))


    #if ('name','url') in test_config:
    #    print('name,url key exists')
    #else:
    #    print('name,url key NOT exists')


    #k = combos.keys()

    #for k in combos:
    # print(k)

    #print(combos.get('okfs_list'))


main()