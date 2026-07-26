# IBM Applied Data Science Capstone — SpaceX Falcon 9 First Stage Landing Prediction

Final project for the IBM Applied Data Science Capstone (Coursera).

SpaceX advertises Falcon 9 launches at $62 million while other providers charge upward of
$165 million. The saving comes from re-using the first stage, so predicting whether the
first stage will land successfully is the same as predicting the cost of a launch. This
project collects the launch data, explores it, visualises it interactively and trains
classifiers to predict the landing outcome.

## Contents

| File | Description |
|---|---|
| `1-jupyter-labs-spacex-data-collection-api.ipynb` | Data collection from the SpaceX REST API |
| `2-jupyter-labs-webscraping.ipynb` | Web scraping the Falcon 9 launch table from Wikipedia with BeautifulSoup |
| `3-labs-jupyter-spacex-Data-wrangling.ipynb` | Data wrangling — the eight landing outcomes reduced to a binary `Class` label |
| `4-jupyter-labs-eda-dataviz.ipynb` | Exploratory data analysis with Matplotlib/Seaborn and one-hot feature engineering |
| `5-jupyter-labs-eda-sql-coursera_sqllite.ipynb` | Exploratory data analysis with SQL against SQLite |
| `6-lab-jupyter-launch-site-location.ipynb` | Interactive Folium maps — launch sites, outcomes and proximities |
| `7-SpaceX-Machine-Learning-Prediction.ipynb` | Logistic Regression, SVM, Decision Tree and KNN, tuned with `GridSearchCV` |
| `spacex_dash_app.py` | Plotly Dash dashboard — site dropdown, success pie chart, payload range slider, payload/outcome scatter |
| `Data_Science_Capstone_Project_Report.pdf` | Final presentation (31 slides) |
| `maps/` | The rendered Folium maps as standalone HTML |
| `figures/` | Every chart, table and screenshot used in the presentation |

## Key results

* Launch success rises from 0% in 2010-2013 to roughly 80% by 2019-2020.
* KSC LC-39A has the best record of any launch site; CCAFS SLC 40 carries most of the
  early failures because it flew the early missions.
* ES-L1, GEO, HEO and SSO show 100% success in this dataset; GTO, the busiest orbit,
  sits near 50%.
* Payloads under 4000 kg land successfully more often than heavier ones.
* All four tuned classifiers reach 83.33% accuracy on the 18-row test set. The Decision
  Tree has the best cross-validated score (86.25%) and is the model taken forward. Its
  confusion matrix shows no false negatives and three false positives.

## Running the dashboard

```bash
pip install pandas dash plotly
python spacex_dash_app.py
```

Then open <http://127.0.0.1:8050/>.

## Note on data sources

`api.spacexdata.com` was returning HTTP 525 at the time these notebooks were executed, so
notebook 1 detects that and falls back to the course's archived extract of the same API
response. The fallback is printed in the notebook output. Wikipedia requires a browser
user agent, which notebook 2 sets explicitly.
