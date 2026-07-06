import { h } from "vue";
import { VDatePicker } from "vuetify/components";

const appsWithComponents = new WeakSet();

function mapDateValue(value, mapper) {
  return Array.isArray(value) ? value.map(mapper) : mapper(value);
}

function toDate(value) {
  if (typeof value !== "string") return value;
  const match = /^(\d{4})-(\d{2})-(\d{2})$/.exec(value);
  return match
    ? new Date(Number(match[1]), Number(match[2]) - 1, Number(match[3]))
    : new Date(value);
}

function toDateString(value) {
  if (!(value instanceof Date)) return value;
  const year = value.getFullYear();
  const month = String(value.getMonth() + 1).padStart(2, "0");
  const day = String(value.getDate()).padStart(2, "0");
  return `${year}-${month}-${day}`;
}

const DatePicker = {
  inheritAttrs: false,
  props: ["modelValue"],
  emits: ["update:modelValue"],
  setup(props, { attrs, emit, slots }) {
    return () =>
      h(
        VDatePicker,
        {
          ...attrs,
          modelValue: mapDateValue(props.modelValue, toDate),
          "onUpdate:modelValue": (value) =>
            emit("update:modelValue", mapDateValue(value, toDateString)),
        },
        slots
      );
  },
};

export function addApp(app) {
  if (appsWithComponents.has(app)) {
    return;
  }

  app.component("IpyvuetifyDatePicker", DatePicker);
  appsWithComponents.add(app);
}
