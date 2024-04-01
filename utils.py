import numbers
import numpy as np
from sklearn.metrics import root_mean_squared_error, r2_score
import matplotlib.pyplot as plt

plt.rcParams.update({
    # 'font.sans-serif': 'Comic Sans MS',
    'font.family': 'serif'
})

def scatter_plot(y_test, y_pred, yax1_name='Depth (m)', xax2_name='GT (m)', yax2_name='MODEL (m)', log_mode=False, model_name=None):

    y_test = np.array(y_test).reshape(-1,)
    y_pred = np.array(y_pred).reshape(-1,)
    print(f'test size: {y_test.shape}, pred size: {y_pred.shape}')

    r = np.corrcoef(y_pred, y_test)[0, 1]
    pbias = 100 * np.sum((y_pred - y_test)) / np.sum(y_test)
    nse = r2_score(y_test, y_pred)
    mse = root_mean_squared_error(y_test, y_pred)
    print(f'NSE: {nse:.4f}, r: {r:.4f}, PBias: {pbias:2.2E}, RMSE: {mse:.4f}')

    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(11, 5), constrained_layout=True)

    ax1.boxplot([y_test, y_pred])
    ax1.set_xticklabels([xax2_name, yax2_name])
    ax1.tick_params(axis='x', labelrotation=0, labelsize=16)
    ax1.set_ylabel(f'{yax1_name}', fontsize=16)
    ax1.grid(True)

    max_value = np.array((y_test, y_pred)).max()

    ax2.scatter(y_test, y_pred, color='teal', edgecolor='steelblue', alpha=0.5)
    ax2.plot([0, max_value], [0, max_value], '--', color='black', linewidth=1.5)

    ax2.set_xlabel(f'{xax2_name}', fontsize=16)
    ax2.tick_params(axis='x', labelsize=16)

    if log_mode:
        ax2.set_yscale('log')
        ax2.set_xscale('log')

    ax2.set_ylabel(f'{yax2_name}', fontsize=16)
    ax2.tick_params(axis='y', labelsize=16)
    ax2.grid(True)

    if model_name is not None:
        f = input('Do you want to save the figure? (Yes/No)')
        
        if f in ['Yes', 'Y', 'yes', 'y']:
            file = input('What format do you want to save the file: ')
            plt.savefig(f'./{model_name}_scplot.{f}', format=f'{file}', bbox_inches='tight', pad_inches=0.1)

    plt.show()
