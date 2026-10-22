import bibleCatalog from '../data/bible_catalog.json';

// Vite dynamic glob imports for code-splitting.
// Each JSON file becomes an isolated async chunk downloaded on demand.
const textModules = import.meta.glob('../data/books/*/text.json');
const kjvModules = import.meta.glob('../data/books/*/kjv.json');
const chapterQaModules = import.meta.glob('../data/books/*/chapter_qa.json');
const bookQaModules = import.meta.glob('../data/books/*/book_qa.json');

// In-memory runtime cache to avoid re-fetching within session
const cache = {
  text: {},
  kjv: {},
  chapterQa: {},
  bookQa: {}
};

/**
 * Returns the full catalog data
 */
export function getBibleCatalog() {
  return bibleCatalog;
}

/**
 * Returns a flat array of all 66 books in canonical order
 */
export function getAllBooks() {
  const books = [];
  bibleCatalog.testaments.forEach((testament) => {
    testament.books.forEach((book) => {
      books.push({
        ...book,
        testamentId: testament.id,
        testamentName: testament.name
      });
    });
  });
  return books;
}

/**
 * Find a book's metadata by its ID (e.g. "GEN"), slug (e.g. "genesis"), or name (e.g. "Genesis")
 */
export function getBookMeta(identifier) {
  if (!identifier) return null;
  const normalized = String(identifier).trim().toLowerCase();
  const all = getAllBooks();
  
  return all.find(b => 
    b.id.toLowerCase() === normalized ||
    b.slug.toLowerCase() === normalized ||
    b.name.toLowerCase() === normalized
  ) || null;
}

/**
 * Find next and previous book given current book ID
 */
export function getAdjacentBooks(bookId) {
  const all = getAllBooks();
  const idx = all.findIndex(b => b.id === bookId);
  if (idx === -1) return { prev: null, next: null };
  return {
    prev: idx > 0 ? all[idx - 1] : null,
    next: idx < all.length - 1 ? all[idx + 1] : null
  };
}

/**
 * Load primary scripture text (EasyEnglish) for a book
 */
export async function loadBookText(bookId) {
  if (!bookId) return null;
  const id = bookId.toUpperCase();
  if (cache.text[id]) return cache.text[id];

  const path = `../data/books/${id}/text.json`;
  const loader = textModules[path];
  
  if (!loader) {
    console.warn(`No text loader found for ${id} at ${path}`);
    return null;
  }

  try {
    const mod = await loader();
    const data = mod.default || mod;
    cache.text[id] = data;
    return data;
  } catch (err) {
    console.error(`Failed to load text for book ${id}:`, err);
    return null;
  }
}

/**
 * Load KJV scripture text for a book
 */
export async function loadBookKjv(bookId) {
  if (!bookId) return null;
  const id = bookId.toUpperCase();
  if (cache.kjv[id]) return cache.kjv[id];

  const path = `../data/books/${id}/kjv.json`;
  const loader = kjvModules[path];
  
  if (!loader) {
    console.warn(`No KJV loader found for ${id} at ${path}`);
    return null;
  }

  try {
    const mod = await loader();
    const data = mod.default || mod;
    cache.kjv[id] = data;
    return data;
  } catch (err) {
    console.error(`Failed to load KJV for book ${id}:`, err);
    return null;
  }
}

/**
 * Load 10-question chapter assessments for a book
 */
export async function loadBookChapterQA(bookId) {
  if (!bookId) return null;
  const id = bookId.toUpperCase();
  if (cache.chapterQa[id]) return cache.chapterQa[id];

  const path = `../data/books/${id}/chapter_qa.json`;
  const loader = chapterQaModules[path];
  
  if (!loader) {
    console.warn(`No chapter QA loader found for ${id} at ${path}`);
    return null;
  }

  try {
    const mod = await loader();
    const data = mod.default || mod;
    cache.chapterQa[id] = data;
    return data;
  } catch (err) {
    console.error(`Failed to load chapter QA for book ${id}:`, err);
    return null;
  }
}

/**
 * Load 50-question comprehensive book assessment for a book
 */
export async function loadBookReviewQA(bookId) {
  if (!bookId) return null;
  const id = bookId.toUpperCase();
  if (cache.bookQa[id]) return cache.bookQa[id];

  const path = `../data/books/${id}/book_qa.json`;
  const loader = bookQaModules[path];
  
  if (!loader) {
    console.warn(`No book QA loader found for ${id} at ${path}`);
    return null;
  }

  try {
    const mod = await loader();
    const data = mod.default || mod;
    cache.bookQa[id] = data;
    return data;
  } catch (err) {
    console.error(`Failed to load book QA for book ${id}:`, err);
    return null;
  }
}
