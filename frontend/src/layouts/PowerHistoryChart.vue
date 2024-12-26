<template>
  <div class="power-history-chart" style="height: 400px">
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
import { ref } from "vue";

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

// 차트 데이터
const chartData = {
  labels: ["12:00", "13:00", "14:00", "15:00", "16:00"], // 시간 데이터
  datasets: [
    {
      label: "전력량 (kWh)",
      backgroundColor: "#f87979",
      data: [40.5, 45.2, 38.3, 42.1, 41.9], // 전력량 데이터
    },
  ],
};

// 차트 옵션
const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      beginAtZero: true,
      title: {
        display: true,
        text: "전력량 (kWh)",
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
