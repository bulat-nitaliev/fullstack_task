<template>
  <div>
    <header class="bg-gray-400 border border-gray-800 h-10">logo</header>
    <div class="container mt-10 mx-auto">
      <form
        class="border-2 border-gray-600 w-2/5 mx-auto bg-blue-100 rounded-lg"
      >
        <div class="flex flex-col w-2/3 gap-3 mt-5 mx-auto pt-5 pb-10">
          <input
            v-model="task.title"
            type="text"
            class="border-2 border-solid border-gray-500 rounded-lg p-2"
            placeholder="Введите имя задачи"
          />
          <div>
            <input
              v-model="task.completed"
              value="1"
              type="radio"
              name="it"
              id="it1"
            />
            <label class="ml-5" for="it1">выполнено </label>
          </div>
          <div>
            <input
              v-model="task.completed"
              value="0"
              type="radio"
              name="it"
              id="it2"
            />
            <label class="ml-5" for="it2">не выполнено </label>
          </div>

          <my-button @click="addTask"> Создать </my-button>
        </div>
      </form>
      <div style="margin: 30px" class="text-center">
        <my-button @click="getTask">получить список заданий </my-button>
      </div>
      <div v-if="lst_task.length">
        <div
          v-for="tsk in lst_task"
          :key="tsk.id"
          class="flex justify-between pl-3 pr-3 pt-3 pb-3 mt-30 border border-gray-500 rounded-md bg-blue-100 m-3"
        >
          <div class="font-bold font-serif">{{ tsk.title }}</div>
          <div>{{ tsk.completed ? "выполнено" : "не выполнено" }}</div>
          <my-button @click="deleteTask(tsk.id)">удалить </my-button>
        </div>
      </div>
      <div
        v-else
        class=" pl-3 pr-3 pt-3 pb-3 mt-30 border border-gray-500 rounded-md bg-blue-100 m-3 text-red-600 font-bold text-center uppercase"
      >
        нет задач
      </div>
    </div>
  </div>
</template>

<script>
import $api from "@/http";
import MyButton from "@/components/MyButton";
export default {
  components: { MyButton },
  name: "App",
  data() {
    return {
      task: {
        title: "",
        completed: null,
      },
      lst_task: [],
    };
  },
  methods: {
    async addTask(e) {
      e.preventDefault();
      const val = this.task.completed ? true : false;
      const data = {
        title: this.task.title,
        completed: val,
      };

      await $api.post("/api/tasks", data);
      this.task = {
        title: "",
        completed: null,
      };
    },
    async getTask() {
      const response = await $api.get("/api/tasks");
      this.lst_task = response.data;
    },
    async deleteTask(id) {
      await $api.delete(`/api/tasks/${id}`);
      this.lst_task = this.lst_task.filter((val) => val.id !== id);
    },
  },
};
</script>

<style></style>
