<template>
  <q-page class="q-pt-sm">
    <div id="result"></div>
    <canvas id="streamChart" class="full-width" style="height: 350px;"></canvas>
    <div class="row gutter-lg q-py-xl layout-padding">
      <div class="col-md-6">
        <q-card class="text-center" :color="checkTemp">
          <q-card-title>
            <q-icon name="fa fa-snowflake" size="64px" color="light-blue-3" class="q-my-md"/>
            <span slot="subtitle" class="uppercase text-dark">Temperature</span>
          </q-card-title>
          <q-card-main>
            <h1>{{curTemp}} °C</h1>
          </q-card-main>
        </q-card>
      </div>
      <div class="col-md-6">
        <q-card class="text-center" :color="checkHum">
          <q-card-title>
            <q-icon name="fa fa-tint" size="64px" color="light-green-8" class="q-my-md"/>
            <span slot="subtitle" class="uppercase text-dark">Humidity</span>
          </q-card-title>
          <q-card-main>
            <h1>{{curHum}} %</h1>
          </q-card-main>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<style>
</style>

<script>
import Chart from 'chart.js'

export default {
  name: 'PageIndex',
  data() {
    return {
      curTemp: 24,
      curHum: 50,
      maxBar: 100,
      mChart: null
    }
  },
  mounted() {
    this.drawTheChart()
    this.streamData()
  },
  methods: {
    drawTheChart() {
      let ctx = document.getElementById("streamChart").getContext('2d');

      this.mChart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: [this.getDateTime(), this.getDateTime()],
          datasets: [
            {
              label: 'Temperature',
              data: [this.curTemp, this.curTemp],
              backgroundColor: 'rgba(129, 212, 250, 0.2)',
              borderColor: 'rgba(129, 212, 250, 1)',
              borderWidth: 1
            },
            {
              label: 'Humidity',
              data: [this.curHum, this.curHum],
              backgroundColor: 'rgba(104, 159, 56, 0.2)',
              borderColor: 'rgba(104, 159, 56, 1)',
              borderWidth: 1
            }
          ]
        },
        options: {
          // animation: false,
          legend: {
            position: 'bottom',
            // labels: {usePointStyle: true}
          },
          tooltips: {
						position: 'nearest',
						mode: 'index'
					},
          scales: {
            xAxes: [{
              ticks: {
                beginAtZero: true
              },
              display: false,
              stacked: true
            }],
            yAxes: [{
              ticks: {
                beginAtZero: true
              },
              display: false,
              stacked: true
            }]
          }
        }
      });
    },
    getDateTime() {
      let today = new Date()
      let date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
      let time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
      return date+' '+time;
    },
    streamData() {
      if (typeof(EventSource) !== "undefined") {
        let source = new EventSource("//localhost:8000/stream/");
        let that = this;

        source.onmessage = function (event) {
          let streamData = JSON.parse(event.data)

          if (that.mChart.data.labels.length > that.maxBar) that.mChart.data.labels.shift()

          that.curTemp = streamData.temp.toFixed(1)
          that.curHum = streamData.hum.toFixed(1)
          that.mChart.data.labels.push(streamData.wkt);
          that.mChart.data.datasets.forEach(dataset => {
            if (dataset.data.length > that.maxBar) {
              dataset.data.shift()
            }

            if (dataset.label == 'Temperature') {
              dataset.data.push(streamData.temp)
            } else {
              dataset.data.push(streamData.hum)
            }
          })

          that.mChart.update()
        };
      } else {
        document.getElementById("result").innerHTML = "Sorry, your browser does not support server-sent events...";
      }
    }
  },
  computed: {
    checkTemp() {
      if (this.curTemp > 24 && this.curTemp <= 26) {
        return 'warning'
      } else if (this.curTemp > 26) {
        return 'negative'
      }
    },
    checkHum() {
      if (this.curHum > 29 && this.curHum < 30) {
        return 'warning'
      } else if (this.curHum > 50 && this.curHum < 51) {
        return 'warning'
      } else if (this.curHum > 51 || this.curHum < 29) {
        return 'negative'
      }
    }
  }
}
</script>
