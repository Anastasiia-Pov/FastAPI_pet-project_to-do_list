import { TTodoForm } from "./types/TodoTypes.ts";

export const getDefaultValues = (): TTodoForm => {
  return {
    text: "",
    is_active: true,
  };
};
