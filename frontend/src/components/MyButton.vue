<template>
  <button
          @click="getTask"
          class="p-3 border border-gray-500 bg-blue-200 font-medium font-sans text-black-300 text-center rounded-md  hover:bg-green-500 transition-colors duration-300"
        >
          <slot></slot>
        </button>
</template>

<script>
export default {
  name: 'my-button'
}
</script>