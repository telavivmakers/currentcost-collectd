# currentcost-collectd

A bridge to collect data from [CurrentCost](http://www.currentcost.com/) using a collectd Python plugin.

## Usage

1. Run the data collection daemon:

    ```bash
    $ python cc-collectd.py
    ```

2. Configure the collectd Python plugin in your `collectd.conf`:

    ```
    <LoadPlugin python>
        Globals true
    </LoadPlugin>

    <Plugin python>
        ModulePath "/path/to/currentcost-collectd"
        LogTraces true
        Interactive true
        Import "currentcost"
        <Module currentcost>
            currentcost
        </Module>
    </Plugin>
    ```

3. View the graphs using your favorite collectd viewer.

4. Profit! (from better controlling your electricity usage.)
