# currentcost-collectd

A bridge to collect data from [CurrentCost](http://www.currentcost.com/) using a collectd Python plugin.

## Usage

1. Configure the collectd Python plugin in your `collectd.conf`:

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

2. Configure the rrdtool plugin (WIP).

3. View the graphs using your favorite collectd data viewer.

4. Profit! (from better controlling your electricity usage.)
