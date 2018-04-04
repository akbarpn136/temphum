<template>
  <q-layout view="lHh Lpr lFf">
    <q-layout-header>
      <q-toolbar color="dark" inverted>
        <q-toolbar-title>
          <q-icon name="fa fa-thermometer-half"/>
          TempHump
        </q-toolbar-title>
        <div class="group">
          <q-btn flat dense round
            @click="doReload()"
            aria-label="Reload">
            <q-icon name="fa fa-redo" />
          </q-btn>
          <q-btn flat dense round
            @click="doOpenModal()"
            aria-label="Reload">
            <q-icon name="fa fa-lightbulb" />
          </q-btn>
        </div>
      </q-toolbar>
    </q-layout-header>

    <q-page-container>
      <q-modal v-model="openModal" minimized content-css="padding: 25px">
        <h4>
          <q-icon name="fa fa-thermometer-half" /> TempHum <q-icon name="fa fa-heart" color="red"/> Open Source
        </h4>
        <p>
          Lorem ipsum dolor sit amet, consectetur adipisicing elit.
        </p>
      </q-modal>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script>
import { openURL } from 'quasar'

export default {
  name: 'LayoutDefault',
  data () {
    return {
      openModal: false
    }
  },
  methods: {
    doReload() {
      window.location.reload()
    },
    doOpenModal() {
      this.openModal = !this.openModal
    }
  }
}
</script>

<style>
</style>
