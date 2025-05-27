<template>
  <div>
    <h1 class="text-2xl font-bold mb-4">Добавить задачу</h1>
    <form @submit.prevent="addTask" class="mb-4">
      <input
        v-model="newTask.title"
        placeholder="Название задачи"
        class="border p-2 mr-2"
      />
      <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded">
        Добавить
      </button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      newTask: { title: "" },
    };
  },
  methods: {
    async addTask() {
      await fetch("/api/tasks", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(this.newTask),
      });
      this.newTask.title = "";
      this.$emit("task-added");
    },
  },
};
</script>
