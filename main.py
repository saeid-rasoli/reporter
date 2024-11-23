import matplotlib.pyplot as plt
import pandas as pd
import itertools
import numpy as np
import matplotlib.ticker as mtick
from matplotlib.ticker import ScalarFormatter, FormatStrFormatter


# fix float format
pd.options.display.float_format = '{:.2f}'.format

def read_csv(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

        # Initialize variables
        dataframes = []
        current_data = []
        header = None

        # Process each line in the file
        for line in lines:
            if line.startswith("Date"):  # Detect a header
                if current_data:  # If there's existing data, create a DataFrame
                    df = pd.DataFrame(current_data, columns=header.split(","))
                    dataframes.append(df)
                header = line.strip()  # Set the new header
                current_data = []  # Reset current data
            else:
                current_data.append(line.strip().split(","))

        # Add the last DataFrame
        if current_data:
            df = pd.DataFrame(current_data, columns=header.split(","))
            dataframes.append(df)

        return dataframes


def main():
    filename = 'all_regions_daily.csv'
    dfs = read_csv(filename)
    tmp_fixed_region_values = list()
    fixed_dfs = list()
    numeric_dfs = list()
    date = list()
    regions = ['tee', 'tew', 'ta', 'is', 'sh', 'ma', 'ah', 'al', 'bl']

    # fix None rows
    for df in dfs:
        df = df.replace(to_replace='None', value=None).dropna()
        fixed_dfs.append(df)

    # drop date and match to fix numeric values to int
    for i, df in enumerate(fixed_dfs):
        date.append(df['Date'])
        df.drop('Date', axis=1, inplace=True)
        df.drop('Match%', axis=1, inplace=True)
        df = df.astype(int)
        numeric_dfs.append(df)
        dfs[i] = df

    # create uniq date
    date = sorted(list(set(itertools.chain(*date))))

    # union of two region to one (tee11 + tee21)
    for i in range(0, len(dfs), 2):
        if i + 1 < len(dfs):
            tmp_fixed_region_values.append(dfs[i].add(dfs[i + 1], fill_value=0))

    # add percent Match to the each region
    for i, df in enumerate(tmp_fixed_region_values):
        tmp_fixed_region_values[i] = df.astype(int)
        percent_match = df['NoRadius'] / df['Total'] * 100
        tmp_fixed_region_values[i]['Match%'] = percent_match


    # figure the summary of radius mismatch
    fig, ax = plt.subplots()

    ## radius mismatch
    plt.title(f'Radius Mismatch Summary Last {len(date)} Days', fontsize=18)
    for i, df in enumerate(tmp_fixed_region_values):
        try:
            percent_dismatch = df.pop('Match%')
            plt.plot(date, percent_dismatch, label=f"{regions[i].upper()} x̄ = {np.mean(percent_dismatch):.2f}%", linewidth=2)
            plt.ylabel('percentage', fontsize=13)
            plt.grid(linestyle='dotted')
            plt.legend()

            # fix ytick formatter
            fmt = '%.0f%%' # Format you want the ticks, e.g. '40%'
            yticks = mtick.FormatStrFormatter(fmt)
            ax.yaxis.set_major_formatter(yticks)
        except:
            print('some regions are not ok!')

    # show and reset each figure
    plt.show()
    plt.clf()

    ## total records
    plt.ticklabel_format(style='plain', useOffset=False)
    plt.title(f'Total Records Count Summary Last {len(date)} Days', fontsize=18)
    for i, df in enumerate(tmp_fixed_region_values):
        try:
            total_count = df.pop('Total')
            plt.plot(date, total_count, label=f"{regions[i].upper()}", linewidth=2)
            plt.ylabel('number of records', fontsize=13)
            plt.grid(linestyle='dotted')
            plt.legend()

        except Exception as err:
            print('some regions are not ok!', err)

    # show and reset each figure
    plt.show()
    plt.clf()

    ## total no radiu
    plt.ticklabel_format(style='plain', useOffset=False)
    plt.title(f'Total No Radius Summary Last {len(date)} Days', fontsize=18)
    for i, df in enumerate(tmp_fixed_region_values):
        try:
            total_count = df.pop('NoRadius')
            plt.plot(date, total_count, label=f"{regions[i].upper()}", linewidth=2)
            plt.ylabel('Number Of No Radius', fontsize=13)
            plt.grid(linestyle='dotted')
            plt.legend()

        except Exception as err:
            print('some regions are not ok!', err)

    # show and reset each figure
    plt.show()
    plt.clf()

    ## total with radius
    plt.ticklabel_format(style='plain', useOffset=False)
    plt.title(f'Total With Radius Summary Last {len(date)} Days', fontsize=18)
    for i, df in enumerate(tmp_fixed_region_values):
        try:
            total_count = df.pop('WithRadius')
            plt.plot(date, total_count, label=f"{regions[i].upper()}", linewidth=2)
            plt.ylabel('Number Of With Radius', fontsize=13)
            plt.grid(linestyle='dotted')
            plt.legend()

        except Exception as err:
            print('some regions are not ok!', err)

    # show and reset each figure
    plt.show()
    plt.clf()

    ## total SPR
    plt.ticklabel_format(style='plain', useOffset=False)
    plt.title(f'Total SPR Summary Last {len(date)} Days', fontsize=18)
    for i, df in enumerate(tmp_fixed_region_values):
        try:
            total_count = df.pop('SPR')
            plt.plot(date, total_count, label=f"{regions[i].upper()}", linewidth=2)
            plt.ylabel('Number Of SPR', fontsize=13)
            plt.grid(linestyle='dotted')
            plt.legend()

        except Exception as err:
            print('some regions are not ok!', err)
    
    # show and reset each figure
    plt.show()
    plt.clf()

    ## total SP
    plt.ticklabel_format(style='plain', useOffset=False)
    plt.title(f'Total SP Summary Last {len(date)} Days', fontsize=18)
    for i, df in enumerate(tmp_fixed_region_values):
        try:
            total_count = df.pop('SP')
            plt.plot(date, total_count, label=f"{regions[i].upper()}", linewidth=2)
            plt.ylabel('Number Of SP', fontsize=13)
            plt.grid(linestyle='dotted')
            plt.legend()

        except Exception as err:
            print('some regions are not ok!', err)

    # show and reset each figure
    plt.show()
    plt.clf()

    ## total SR
    plt.ticklabel_format(style='plain', useOffset=False)
    plt.title(f'Total SR Summary Last {len(date)} Days', fontsize=18)
    for i, df in enumerate(tmp_fixed_region_values):
        try:
            total_count = df.pop('SR')
            plt.plot(date, total_count, label=f"{regions[i].upper()}", linewidth=2)
            plt.ylabel('Number Of SR', fontsize=13)
            plt.grid(linestyle='dotted')
            plt.legend()

        except Exception as err:
            print('some regions are not ok!', err)

    # show and reset each figure
    plt.show()
    plt.clf()

    ## total S
    plt.ticklabel_format(style='plain', useOffset=False)
    plt.ticklabel_format(style='plain', useOffset=False)
    plt.title(f'Total S Summary Last {len(date)} Days', fontsize=18)
    for i, df in enumerate(tmp_fixed_region_values):
        try:
            total_count = df.pop('S')
            plt.plot(date, total_count, label=f"{regions[i].upper()}", linewidth=2)
            plt.ylabel('Number Of S', fontsize=13)
            plt.grid(linestyle='dotted')
            plt.legend()

        except Exception as err:
            print('some regions are not ok!', err)


    plt.xlabel('Date', fontsize=13)
    plt.xticks(rotation=40)
    plt.show()

    # TODO: fix each region rows (add zero mock row to needed region)


if __name__ == '__main__':
    main()
