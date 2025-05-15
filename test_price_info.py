import price_info as PInfo


def test_cost_of_fruits():
    fruit_name='watermelon'
    fruit_quantity=5
    expected_result=32.50
    test_result=PInfo.cost_of_fruits(fruit_name,fruit_quantity)
    assert(test_result==expected_result)
    #shorter way
    #assert(PInfo.cost_of_fruit('watermelon',5)==32.50)

def test_total_cost_shopping():
    expected_result=46.75
    test_result=PInfo.total_cost_shopping()
    assert(test_result==expected_result)