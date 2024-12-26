<template>
  <div
    class="power-history-chart"
    style="height: 400px"
    v-if="chartData && chartData.labels.length"
  >
    <Line :data="chartData" :options="chartOptions" />
  </div>
</template>

<style lang="scss" scoped>
.power-history-chart {
  width: 100%;
  height: 100%;
}
</style>

<script setup>
import { Line } from "vue-chartjs";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { ref, watch, onMounted } from "vue";

const props = defineProps({
  powerData: {
    type: Array,
    default: [],
  },
});

// 차트 데이터
const chartData = ref({
  labels: [], // 시간 데이터
  datasets: [
    {
      label: "전력소비 (kWh)",
      backgroundColor: "#ec4899",
      data: [], // 전력량 데이터
    },
  ],
});

watch(
  () => props.powerData,
  () => {
    console.log("props.powerData", props.powerData);
    const labels = props.powerData.map((data) => data.timestamp);
    const data = props.powerData.map((data) => data.value);

    chartData.value = {
      labels: labels, // 시간 데이터
      datasets: [
        {
          label: "전력소비 (kWh)",
          backgroundColor: "#ec4899",
          data: data, // 전력량 데이터
        },
      ],
    };
  },
  { immediate: true, deep: true }
);

// Chart.js 컴포넌트 등록
ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
);

// 차트 옵션
const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      beginAtZero: true,
      title: {
        display: true,
        text: "전력소비 (kWh)",
      },
    },
    x: {
      title: {
        display: true,
        text: "시간",
      },
    },
  },
};
</script>
