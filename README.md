# election2020
Election audit scripts and docs for checking for anomalies

Sections:

## Where and how to download registration and results

## Things to look for

- duplicate voter registrations - did we get duplicate votes?
- ratio between party members voting / votes for party candidate by precinct

So, we want both election results by precinct and voter participation by party and precinct.  See sources below.

## Election Results Data Sources

There is no single nationwide source for precinct level data.  It is available from some states, and for those that do not make it available at the state level, in particular FL, TX, NY, PA, UT, MI, MO, CA, OH, http://openelections.net will be working on collating and making the data available from  to download.

For 2016 data, there is full precinct level data for comparison: https://dataverse.harvard.edu/dataverse/medsl_president 

https://electionlab.mit.edu/data#tools has a good list of general sources

https://github.com/openelections has useful code 

### PA
https://www.electionreturns.pa.gov/ReportCenter/Reports. - breakdown by County
To get precinct level results, it may be necessary to look at the county websites
http://www.buckscounty.org/docs/default-source/boe/2020generalprimarycertifiedelectionresultsbypercinct.pdf?sfvrsn=64d90fef_0

or we can wait for openelections.net to parse it and make it available.

### GA
https://sos.ga.gov/index.php/Elections/current_and_past_elections_results will have links
ex: https://results.enr.clarityelections.com/GA/DeKalb/105081/web.259135/#/reporting?v=260887%2F
can download XLS from each county with precinct breakdowns

### MI
Michigan may allow single download of all precinct data!
ie https://miboecfr.nictusa.com/cfr/presults/2018GEN.zip
https://miboecfr.nictusa.com/cgi-bin/cfr/precinct_srch.cgi?elect_year_type=2018GEN&county_code=00&Submit=Search

Also has single page with links to PDF per county with per-precinct data
ex: https://www.michigan.gov/sos/0,4670,7-127-1633_8722-486915--,00.html
search by precinct: https://miboecfr.nictusa.com/cgi-bin/cfr/precinct_srch.cgi

## FL
Has precinct level election results easily downloadable
https://dos.myflorida.com/elections/data-statistics/elections-data/precinct-level-election-results/


## Voter Registration & Participation Data Sources

(search for 'voter participation database' or 'voter registration database' + state )
General info: https://www.ncsl.org/research/elections-and-campaigns/access-to-and-use-of-voter-registration-lists.aspx

### FL
https://dos.myflorida.com/elections/data-statistics/elections-data/

https://dos.myflorida.com/elections/data-statistics/elections-data/precinct-level-election-results/

Request voter reg data: https://dos.myflorida.com/elections/data-statistics/voter-registration-statistics/voter-extract-disk-request/
```
requested from DivElections@dos.myflorida.com on 10/24/20
Could be picked up 10/28
Address: The R.A. Gray Building
500 South Bronough Street, Room 316
Tallahassee, FL  32399-0250
```
### PA
https://www.pavoterservices.pa.gov/pages/purchasepafullvoterexport.aspx
(we have the full download from Oct 25; ask in discord)

### WI
https://elections.wi.gov/clerks/svrs/voter-data

https://badgervoters.wi.gov/  $25 + 5/1000 voter records

https://badgervoters.wi.gov/
 

### CO
https://www.sos.state.co.us/pubs/info_center/fees/elections.html

https://www.sos.state.co.us/pubs/elections/forms/dataRequests.pdf

### GA
https://sos.ga.gov/index.php/elections/order_voter_registration_lists_and_files
(whole state costs $250; has last election voted, not clear when this is updated - phone 844.753.7825)

### MN
https://www.sos.state.mn.us/election-administration-campaigns/data-maps/registered-voter-list-requests/
whole state is $46 but only MN voters may order it.
(A scrutineers volunteer is getting this for us)

### MT
https://app.mt.gov/voterfile/  ($1000 for whole state)

### NC
https://dl.ncsbe.gov/index.html?prefix=data/Snapshots/
seems to be free, but not updated too often
also Voter History Data - https://www.ncsbe.gov/results-data/voter-history-data

### SC
https://info.scvotes.sc.gov/eng/saleabledata/home.aspx
(must be a South Carolina voter)

## Scripts and libraries

## For reference

http://cooperation.org/askthevoters

## Community

Discord: https://discord.gg/92K4nFg

Trello: https://trello.com/b/JSH41nyv/election2020
