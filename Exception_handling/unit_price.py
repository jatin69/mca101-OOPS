import sys

def main():

    '''
    Objective: To compute price per unit weight of an item
    Input Parameter: None
    Return Value: None

    '''
    price = input('Enter price of item purchased: ')
    weight = input('Enter weight of item purchased: ')

    try:
        if price == '':
            price =None
        try:
            price = float(price)
        
        except ValueError:
            print('Invalid inputs: ValueError')

        if weight == '':
            weight =None

        try:
            weight = float(weight)

        except ValueError:
            print('Invalid inputs: ValueError')

        assert price >= 0 and weight >= 0

        result = price / weight

    except TypeError:
        print('Invalid inputs: TypeError')

    except ZeroDivisionError:
        print('Invalid inputs: ZeroDivisionError')

    except:
        print(str(sys.exc_info()))

    else:
        print('Price per unit weight: ', result)

if __name__ == '__main__':
    main()
