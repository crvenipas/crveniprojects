import pandas as pd
import numpy as np
import argparse
import os
import glob
import matplotlib.pyplot as plt

def analyze_file(filepath, t_column='t_years'):
    df = pd.read_csv(filepath, sep='\s+')
    ages = -df[t_column].values

    mean_age = np.mean(ages)
    std_age = np.std(ages, ddof=1)
    median_age = np.median(ages)
    p5_age, p95_age = np.percentile(ages, [5, 95])

    stats = {
        'mean_age': mean_age,
        'std_age': std_age,
        'median_age': median_age,
        'p5_age': p5_age,
        'p95_age': p95_age,
        'ages': ages
    }
    return stats

def save_results(name, stats, output_dir, plot_hist=True, bins=100):
    t_mean_kyr = stats['mean_age'] / 1000
    std_kyr = stats['std_age'] / 1000
    t_med_kyr = stats['median_age'] / 1000
    t_p5_kyr = stats['p5_age'] / 1000
    t_p95_kyr = stats['p95_age'] / 1000

    plus = t_p95_kyr - t_med_kyr
    minus = t_med_kyr - t_p5_kyr

    os.makedirs(output_dir, exist_ok=True)

    summary_path = os.path.join(output_dir, 'ages_summary.txt')
    with open(summary_path, 'a') as f:
        summary_line = (f"{name}\n"
                        f"  T_{{mean}} = {t_mean_kyr:.0f} \pm {std_kyr:.0f} kyr\n"
                        f"  T_{{med}}  = {t_med_kyr:.0f}^{{+{plus:.0f}}}_{{-{minus:.0f}}} kyr\n\n")
        f.write(summary_line)

    if plot_hist:
        plt.figure(figsize=(6,4))
        plt.hist(stats['ages'] / 1000, bins=bins)
        plt.xlabel('Age (thousands of years)')
        plt.ylabel('Number of clones')
        plt.title(f'Age distribution: {name}')
        plt.grid(True)

        hist_path = os.path.join(output_dir, f"{name}_histogram.png")
        plt.savefig(hist_path)
        plt.close()

def main():
    parser = argparse.ArgumentParser(
        description='Batch process asteroid pair folders to compute age estimates.'
    )
    parser.add_argument(
        'root',
        help='Path to the root folder containing asteroid pair subfolders.'
    )
    parser.add_argument(
        '--t-column', default='t_years',
        help="Column name of time values (default: 't_years')"
    )
    parser.add_argument(
        '--nohist', action='store_true',
        help='Do not plot and save histograms.'
    )
    parser.add_argument(
        '--bins', type=int, default=100,
        help='Number of bins for histograms (default: 100)'
    )
    args = parser.parse_args()

    for subdir in sorted(os.listdir(args.root)):
        pair_path = os.path.join(args.root, subdir)
        if not os.path.isdir(pair_path):
            continue

        file_dper = glob.glob(os.path.join(pair_path, "protocol_dnode_dper_*.txt"))
        file_dper = [f for f in file_dper if 'aver' not in os.path.basename(f)]

        file_aver = glob.glob(os.path.join(pair_path, "protocol_dnode_dper_aver_*.txt"))
        file_rho = glob.glob(os.path.join(pair_path, "protocol_rho_min_*.txt"))

        files = file_dper[:1] + file_aver[:1] + file_rho[:1]

        if len(files) != 3:
            print(f"[!] Пропущено: {subdir} — найдено {len(files)} из 3 нужных файлов")
            continue

        print(f"\n[subdir: {subdir}] Обработка файлов...")

        output_dir = os.path.join(pair_path, f"results_{subdir}")
        if os.path.exists(os.path.join(output_dir, 'ages_latex.txt')):
            os.remove(os.path.join(output_dir, 'ages_latex.txt'))

        for filepath in files:
            stats = analyze_file(filepath, t_column=args.t_column)
            short_name = os.path.splitext(os.path.basename(filepath))[0]
            save_results(short_name, stats, output_dir, plot_hist=not args.nohist, bins=args.bins)

        print(f"  ✔ Результаты сохранены в {output_dir}")

if __name__ == '__main__':
    main()
