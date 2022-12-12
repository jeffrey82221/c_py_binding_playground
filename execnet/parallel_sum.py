PARALLEL_CNT = 1000
def batchwise_generator(gen, batch_size=100):
    batch = []
    for i, element in enumerate(gen):
        batch.append(element)
        if i % batch_size == (batch_size - 1):
            yield batch
            del batch
            batch = []
    if batch:
        yield batch

def batch_sum(inputs):
    result = 0
    for i in inputs:
        result += i
    return result

def sum(input_array):
    batch_pipe = batchwise_generator(input_array, batch_size=len(input_array)/PARALLEL_CNT)
    sum_result = 0
    for batch in batch_pipe:
        sum_result += batch_sum(batch)
    return sum_result