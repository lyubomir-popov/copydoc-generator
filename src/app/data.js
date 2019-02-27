import * as markup from "./markup";

const stripTypes = [
  {
    name: "hero",
    label: "Hero"
  },
  {
    name: "key-features",
    label: "Key features"
  },
  {
    name: "proposition",
    label: "Proposition"
  },
  {
    name: "detail",
    label: "Detail"
  },
  {
    name: "embed",
    label: "Embed"
  },
  {
    name: "comparison",
    label: "Comparison"
  },
  {
    name: "credibility",
    label: "Credibility"
  },
  {
    name: "links",
    label: "Links"
  },
  {
    name: "instructions",
    label: "Instructions"
  },
  {
    name: "tail",
    label: "Tail"
  }
];

const stripExamples = [
  {
    type: "hero",
    name: "Hero 1",
    jsx: markup.Hero1
  },
  {
    type: "hero",
    name: "Hero 2",
    jsx: markup.Hero2
  },
  {
    type: "key-features",
    name: "Key features 1",
    jsx: markup.KeyFeatures1
  },
  {
    type: "key-features",
    name: "Key features 2",
    jsx: markup.KeyFeatures2
  }
];

export { stripTypes, stripExamples };
