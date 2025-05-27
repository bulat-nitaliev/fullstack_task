<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">Список задач</h1>
    <ul>
      <li v-for="task in tasks" :key="task.id" class="mb-2 p-2 border rounded">
        {{ task.title }}
        <button
          @click="deleteTask(task.id)"
          class="ml-4 bg-red-500 text-white px-2 py-1 rounded"
        >
          Удалить
        </button>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      tasks: [],
    };
  },
  async created() {
    await this.fetchTasks();
  },
  methods: {
    async fetchTasks() {
      const response = await fetch("/api/tasks");
      this.tasks = await response.json();
    },
    async deleteTask(id) {
      await fetch(`/api/tasks/${id}`, { method: "DELETE" });
      await this.fetchTasks();
    },
  },
};
</script>
