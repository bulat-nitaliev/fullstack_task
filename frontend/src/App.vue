<template>
  <div class="container mx-auto p-4">
    <AddTask @task-added="fetchTasks" />
    <TaskList ref="taskList" />
  </div>
</template>

<script>
import AddTask from "@/components/AddTask.vue";
import TaskList from "@/components/TaskList.vue";

export default {
  components: {
    AddTask,
    TaskList,
  },
  methods: {
    fetchTasks() {
      this.$refs.taskList.fetchTasks();
    },
  },
};
</script>
<style></style>
