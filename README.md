
Quick experiment for categorising values using an LLM.

## Dependencies

- Python 3
- [`uv`](https://docs.astral.sh/uv/) for running the script
- [`ollama`](https://ollama.com/)

## Data

The values in demo.csv are randomly generated.

## Run locally

    uv sync
    uv run analyse.py

## Example output

```
['Taylor', 'Emily', '145 Oakwood Drive', '23 Parkside Cottages', 'Wimbury', 'Hampshire', 'BN98 3YT', '2006', 'Sat', 'May 06 2006', '2006-May-06', '2006-05-06']
['last_name', 'first_name', 'address', 'address', 'address', 'address', 'address', 'date', 'day_of_week', 'date', 'date', 'date']

['Smith', 'James', '21 Willowdale Close', 'The Greenhouses', 'Littleton Mill', 'Suffolk', 'DG45 9NH', '1942', 'Sat', 'Aug 29 1942', '1942-Aug-29', '1942-08-29']
['last_name', 'first_name', 'address', 'address', 'address', 'address', 'address', 'date', 'day_of_week', 'date', 'date', 'date']

['Johnson', 'Olivia', '92 Chestnut Avenue', '17 Silver Birch Lane', 'Langford-on-the-Marsh', 'Essex', 'MK76 4GU', '2010', 'Sun', 'Jan 10 2010', '2010-Jan-10', '2010-01-10']
['last_name', 'first_name', 'address', 'address', 'address', 'address', 'address', 'year', 'day_of_week', 'date', 'date', 'date']

['Williams', 'William', '37 Firs Road', 'Hawthorn Cottage', 'Nettlethorpe', 'Kent', 'CF67 8WD', '2014', 'Mon', 'Jul 14 2014', '2014-Jul-14', '2014-07-14']
['last_name', 'first_name', 'address', 'address', 'address', 'address', 'address', 'year', 'day_of_week', 'date', 'date', 'date']

['Brown', 'Ava', '11 Maplewood Court', '23 Cedar Close', 'Ashdown Forest', 'Sussex', 'KY53 6BX', '2017', 'Mon', 'Mar 20 2017', '2017-Mar-20', '2017-03-20']
['color', 'first_name', 'address', 'address', 'address', 'address', 'address', 'year', 'day_of_week', 'date', 'date', 'date']

['Davis', 'George', '56 Rowan Way', 'The Old Mill House', 'Badenham', 'Cambridgeshire', 'DN64 7ER', '1962', 'Wed', 'Feb 14 1962', '1962-Feb-14', '1962-02-14']
['last_name', 'first_name', 'address', 'address', 'address', 'address', 'address', 'date', 'day_of_week', 'date', 'date', 'date']

['Wilson', 'Isabella', '25 Willow Tree Close', 'Oakwood Farm Cottages', 'Great Saling', 'Essex', 'EX38 4HQ', '2006', 'Sat', 'Dec 30 2006', '2006-Dec-30', '2006-12-30']
['last_name', 'first_name', 'address', 'address', 'address', 'address', 'address', 'year', 'day_of_week', 'date', 'date', 'date']

['Harris', 'Thomas', '42 Bramble Hill', '19 Pineview Road', 'Tadlow', 'Hertfordshire', 'TR21 9GP', '1998', 'Sun', 'Jun 28 1998', '1998-Jun-28', '1998-06-28']
['last_name', 'first_name', 'address', 'address', 'address', 'address', 'address', 'year', 'day_of_week', 'date', 'date', 'date']
```
