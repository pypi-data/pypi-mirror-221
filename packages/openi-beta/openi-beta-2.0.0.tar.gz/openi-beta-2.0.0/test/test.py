def download_with_tqdm(
        filepath: str,
        **kwargs
):
    
    print(f"filepath: {filepath}")

    print(f'i: {kwargs.keys()}')


download_with_tqdm('1234', i='0000', k='9999')