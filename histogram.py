def create_histogram(file, band_number):
    """Method receives a file and number of bands to print a histogram"""
    nums = get_nums_from_file(file)

    #  Return a print statement to let user know number of bands is invalid
    if band_number < 2:
        print("Error: Band number must be greater than or equal to 2.")
        return None

    bands = get_bands(nums, band_number)
    print_histogram(bands)

def get_nums_from_file(file):
    nums = []
    with open(file) as fh:
        for line in fh.readlines():
            nums.append(float(line.strip()))
    return nums

def get_bands(nums, band_number):
    """Determines band size based on number of numbers and band number."""
    bands = {}
    min_num = min(nums)
    max_num = max(nums)

    # Calculate band size using midpoint
    band_size = (max_num - min_num) / (band_number - 1)
    
    # Create histogram
    band_min = min_num - (band_size / 2)
    
    for index in range(band_number):
        band_max = (index * band_size) + min_num + (band_size / 2)
        bands[(band_min, band_max)] = 0
        band_min = band_max
    
    for num in nums:
        if get_band_value(num, bands) is None:
            breakpoint()
        bands[get_band_value(num, bands)] +=1

    return bands

def get_band_value(num, bands):

    for band in bands:
        if band[0] <= num <= band[1]:
            band_value = band
            return band_value

    return None


def print_histogram(bands):
    for band in sorted(bands.keys()):
        band_range = f"{round(band[0],1)}-{round(band[1],1)}"
        print(f"{band_range.rjust(15)} | {'*' * bands[band]}")


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(description='Create a histogram')
    parser.add_argument('-b', '--band-number', default=10, type=float)
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)

    if file.is_file():
        create_histogram(file, args.band_number)
    else:
        print(f"{file} does not exist!")
        exit(1)
